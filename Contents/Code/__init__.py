#############
# credit to DiegoV in New Zealand for some nice simple code to work from
#############
ART = 'art-default.jpg'
ICON = 'icon-default.png'

# PLAYLIST_URL_AAC = 'http://icy-e-02-cr.sharp-stream.com:8000/planetrock.aac'
# PLAYLIST_URL_MP3 = 'http://tx.sharp-stream.com/icecast.php?i=planetrock.mp3'

Radio1 = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p'
Radio1Xtra = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1xtra_mf_p'
Radio2 = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p'
Radio3 = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio3_mf_p'
Radio4 = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4fm_mf_p'
Radio4LW = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4lw_mf_p'
Radio4Extra = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4extra_mf_p'
Radio5Live = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio5live_mf_p'
Radio5LiveSportsExtra = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio5extra_mf_p'
Radio6Music = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_6music_mf_p'
WorldService = 'http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-eieuk'


PREFIX = '/music/bbcradio'


def Start():
    '''
    The Start function is initially called by the PMS framework to initialize the plugin.
    This includes setting up the Plugin static instance along with the displayed artwork.
    '''
    # Initialize the plugin
    Plugin.AddViewGroup('the_view_group', viewMode='List', mediaType='items')

    # Setup the artwork associated with the plugin
    ObjectContainer.title1 = 'BBC Radio'
    ObjectContainer.art = R(ART)
    ObjectContainer.view_group = 'the_view_group'

    # DirectoryObject.thumb = R(ICON)

    TrackObject.thumb = R(ICON)
    TrackObject.art = R(ART)


@handler(PREFIX, 'BBC Radio')
def MainMenu():
    '''
    MainMenu populates the menu with the buttons that the user will use to select the station that they wish to listen to.
    '''
    # Would love to call this periodically to update the channel background art, but not possible
    # oc.art = HTTP.Request('http://radioparadise.com/readtxt.php').content

    # PLAYLIST_URL_MP3 = Prefs['mp3_url']

    oc = ObjectContainer()
    oc.add(CreateTrackObject(url=Radio1, title='Play BBC Radio 1', fmt='mp3'))
    oc.add(CreateTrackObject(url=Radio1Xtra, title='Play BBC Radio 1Xtra', fmt='mp3'))
    oc.add(CreateTrackObject(url=Radio2, title='Play BBC Radio 2', fmt='mp3'))
    oc.add(CreateTrackObject(url=Radio3, title='Play BBC Radio 3', fmt='mp3'))
    oc.add(CreateTrackObject(url=Radio4, title='Play BBC Radio 4', fmt='mp3'))
    oc.add(CreateTrackObject(url=Radio4LW, title='Play BBC Radio 4 LW', fmt='mp3'))
    oc.add(CreateTrackObject(url=Radio4Extra, title='Play BBC Radio 4 Extra', fmt='mp3'))
    oc.add(CreateTrackObject(url=Radio5Live, title='Play BBC Radio 5 live', fmt='mp3'))
    oc.add(CreateTrackObject(url=Radio5LiveSportsExtra, title='Play BBC Radio 5 live sports extra', fmt='mp3'))
    oc.add(CreateTrackObject(url=Radio6Music, title='Play BBC Radio 6 Music', fmt='mp3'))
    oc.add(CreateTrackObject(url=WorldService, title='Play BBC Radio World Service', fmt='mp3'))

    # removed AAC stream as AAC audio playback does not appear to work at the moment
    # oc.add(CreateTrackObject(url=PLAYLIST_URL_AAC, title='Planet Rock AAC Stream', fmt='aac'))

    return oc


def CreateTrackObject(url, title, fmt, include_container=False):
    '''
    CreateTrackObject creates
    Inputs:
    -------
        url - URL
            URL of stream

        title - String
            Title of the stream

        fmt - String
            Format of the stream

        include_container - boolean
            If true return the track_object inside an ObjectContainer
    Returns:
    -------
        TrackObject - Object containing Callback and Media Object

    '''
    # choose container and codec to use for the supplied format
    if fmt == 'mp3':
        container = Container.MP3
        audio_codec = AudioCodec.MP3
    elif fmt == 'aac':
        container = Container.MP4
        audio_codec = AudioCodec.AAC

    # create TrackObject for stream
    track_object = TrackObject(
        key=Callback(CreateTrackObject, url=url, title=title, fmt=fmt, include_container=True),
        rating_key=url,
        title=title,
        items=[
            MediaObject(
                parts=[
                    PartObject(key=Callback(PlayAudio, url=url, ext=fmt))
                ],
                container=container,
                audio_codec=audio_codec,
                audio_channels=2
            )
        ]
    )

    if include_container:
        return ObjectContainer(objects=[track_object])
    else:
        return track_object


def PlayAudio(url):
    '''
    PlayAudio
    Inputs:
    -------
        url - URL of stream
    '''
    return Redirect(url)
