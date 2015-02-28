#############
# credit to DiegoV in New Zealand for some nice simple code to work from
#############
ART = 'art-default.jpg'
ICON = 'icon-default.png'

# PLAYLIST_URL_AAC = 'http://icy-e-02-cr.sharp-stream.com:8000/planetrock.aac'
# PLAYLIST_URL_MP3 = 'http://tx.sharp-stream.com/icecast.php?i=planetrock.mp3'

'''
URLs of radio streams that will be used by the plug in.
'''
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

# EXTM3U
# EXTINF:-1,[*R1] BBC Radio 1
Radio1_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_one.m3u8'
# EXTINF:-1,[*R1X] BBC Radio 1Xtra
Radio1Xtra_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_1xtra.m3u8'
# EXTINF:-1,[*R2] BBC Radio 2
Radio2_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_two.m3u8'
# EXTINF:-1,[*R3] BBC Radio 3
Radio3_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_three.m3u8'
# EXTINF:-1,[*R4] BBC Radio 4 FM
Radio4_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_fourfm.m3u8'
# EXTINF:-1,[*R4X] BBC Radio 4 Extra
Radio4Extra_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_four_extra.m3u8'
# EXTINF:-1,[*R4L] BBC Radio 4 LW
Radio4LW_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_fourlw.m3u8'
# EXTINF:-1,[*R5] BBC Radio 5 Live
Radio5Live_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_five_live.m3u8'
# EXTINF:-1,[*R5X] BBC Radio 5 Live Sports Extra
Radio5LiveSportsExtra_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_five_live_sports_extra.m3u8'
# EXTINF:-1,[*R6] BBC Radio 6 Music
Radio6Music_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_6music.m3u8'
# EXTINF:-1,[*AN] BBC Asian Network
RadioASNNetwork_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_asian_network.m3u8'
# EXTINF:-1,[*SC] BBC Radio Scotland FM
RadioScotland_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_scotland_fm.m3u8'
# EXTINF:-1,[*SCM] BBC Radio Scotland MW
RadioScotlandMW_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_scotland_mw.m3u8'
# EXTINF:-1,[*NG] BBC Radio Nan Gaidheal
RadioNanGaidheal_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_nan_gaidheal.m3u8'
# EXTINF:-1,[*UL] BBC Radio Ulster
RadioUlster_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_ulster.m3u8'
# EXTINF:-1,[*FO] BBC Radio Foyle
RadioFoyle_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_foyle.m3u8'
# EXTINF:-1,[*WA] BBC Radio Wales
RadioWales_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_wales_fm.m3u8'
# EXTINF:-1,[*CY] BBC Radio Cymru
RadioCymru_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_cymru.m3u8'
# EXTINF:-1,[*BE] BBC Radio Berkshire
RadioBerkshire_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_berkshire.m3u8'
# EXTINF:-1,[*BR] BBC Radio Bristol
RadioBristol_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_bristol.m3u8'
# EXTINF:-1,[*CA] BBC Radio Cambridge
RadioCambridge_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_cambridge.m3u8'
# EXTINF:-1,[*CO] BBC Radio Cornwall
RadioCornwall_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_cornwall.m3u8'
# EXTINF:-1,[*CW] BBC Radio Coventry Warwickshire
RadioCoventryWarwickshire_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_coventry_warwickshire.m3u8'
# EXTINF:-1,[*CU] BBC Radio Cumbria
RadioCumbria_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_cumbria.m3u8'
# EXTINF:-1,[*DE] BBC Radio Derby
RadioDerby_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_derby.m3u8'
# EXTINF:-1,[*DV] BBC Radio Devon
RadioDevon_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_devon.m3u8'
# EXTINF:-1,[*ES] BBC Radio Essex
RadioEssex_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_essex.m3u8'
# EXTINF:-1,[*GL] BBC Radio Gloucestershire
RadioGloucestershire_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_gloucestershire.m3u8'
# EXTINF:-1,[*GU] BBC Radio Guernsey
RadioGuernsey_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_guernsey.m3u8'
# EXTINF:-1,[*HW] BBC Radio Hereford Worcester
RadioHerefordWorcester_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_hereford_worcester.m3u8'
# EXTINF:-1,[*HU] BBC Radio Humberside
RadioHumberside_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_humberside.m3u8'
# EXTINF:-1,[*JE] BBC Radio Jersey
RadioJersey_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_jersey.m3u8'
# EXTINF:-1,[*KE] BBC Radio Kent
RadioKent_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_kent.m3u8'
# EXTINF:-1,[*LA] BBC Radio Lancashire
RadioLancashire_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_lancashire.m3u8'
# EXTINF:-1,[*LE] BBC Radio Leeds
RadioLeeds_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_leeds.m3u8'
# EXTINF:-1,[*LC] BBC Radio Leicester
RadioLeicester_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_leicester.m3u8'
# EXTINF:-1,[*LI] BBC Radio Lincolnshire
RadioLincolnshire_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_lincolnshire.m3u8'
# EXTINF:-1,[*LO] BBC Radio London
RadioLondon_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_london.m3u8'
# EXTINF:-1,[*MA] BBC Radio Manchester
RadioManchester_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_manchester.m3u8'
# EXTINF:-1,[*ME] BBC Radio Merseyside
RadioMerseyside_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_merseyside.m3u8'
# EXTINF:-1,[*NE] BBC Radio Newcastle
RadioNewcastle_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_newcastle.m3u8'
# EXTINF:-1,[*NO] BBC Radio Norfolk
RadioNorfolk_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_norfolk.m3u8'
# EXTINF:-1,[*NH] BBC Radio Northampton
RadioNorthampton_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_northampton.m3u8'
# EXTINF:-1,[*NT] BBC Radio Nottingham
RadioNottingham_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_nottingham.m3u8'
# EXTINF:-1,[*OX] BBC Radio Oxford
RadioOxford_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_oxford.m3u8'
# EXTINF:-1,[*SH] BBC Radio Sheffield
RadioSheffield_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_sheffield.m3u8'
# EXTINF:-1,[*SR] BBC Radio Shropshire
RadioShropshire_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_shropshire.m3u8'
# EXTINF:-1,[*SL] BBC Radio Solent
RadioSolent_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_solent.m3u8'
# EXTINF:-1,[*SS] BBC Radio Somerset Sound
RadioSomerset_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_somerset_sound.m3u8'
# EXTINF:-1,[*ST] BBC Radio Stoke
RadioStoke_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_stoke.m3u8'
# EXTINF:-1,[*SU] BBC Radio Suffolk
RadioSuffolk_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_suffolk.m3u8'
# EXTINF:-1,[*SR] BBC Radio Surrey
RadioSurrey_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_surrey.m3u8'
# EXTINF:-1,[*SX] BBC Radio Sussex
RadioSussex_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_sussex.m3u8'
# EXTINF:-1,[*TE] BBC Radio Tees
RadioTees_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_tees.m3u8'
# EXTINF:-1,[*3C] BBC Radio Three Counties
Radio3Counties_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_three_counties_radio.m3u8'
# EXTINF:-1,[*WI] BBC Radio Wiltshire
RadioWiltshire_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_wiltshire.m3u8'
# EXTINF:-1,[*WM] BBC Radio West Midlands
RadioWestMidlands_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_wm.m3u8'
# EXTINF:-1,[*YO] BBC Radio York
RadioYork_HLS = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_york.m3u8'
# EXTINF:-1,[*WS] BBC World Service
RadioWorldService_HLS = 'http://bbcwsen-lh.akamaihd.net/i/WSEIEUK_1@189911/master.m3u8'


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
    # HLS Streams
    oc.add(CreateTrackObject(url=Radio1_HLS, title='BBC Radio 1 (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=Radio1Xtra_HLS, title='Play BBC Radio 1 Extra (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=Radio2_HLS, title='Play BBC Radio 2 (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=Radio3_HLS, title='Play BBC Radio 3 (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=Radio4_HLS, title='Play BBC Radio 4 (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=Radio4Extra_HLS, title='Play BBC Radio 4 Extra (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=Radio4LW_HLS, title='Play BBC Radio 4 LW (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=Radio5Live_HLS, title='Play BBC Radio 5 Live (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=Radio5LiveSportsExtra_HLS, title='Play BBC Radio 5 Live Sports Extra (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=Radio6Music_HLS, title='Play BBC Radio 6 Music (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioASNNetwork_HLS, title='Play BBC Radio Asian Network (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioScotland_HLS, title='Play BBC Radio Scotland (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioScotlandMW_HLS, title='Play BBC Radio Scotland MW (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioNanGaidheal_HLS, title='Play BBC Radio Nan Gaidheal (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioUlster_HLS, title='Play BBC Radio Ulster (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioFoyle_HLS, title='Play BBC Radio Foyle (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioWales_HLS, title='Play BBC Radio Wales (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioCymru_HLS, title='Play BBC Radio Cymru (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioBerkshire_HLS, title='Play BBC Radio Berkshire (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioBristol_HLS, title='Play BBC Radio Bristol (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioCambridge_HLS, title='Play BBC Radio Cambridge (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioCornwall_HLS, title='Play BBC Radio Cornwall (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioCoventryWarwickshire_HLS, title='Play BBC Radio Coventry Warwickshire (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioCumbria_HLS, title='Play BBC Radio Cumbria (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioDerby_HLS, title='Play BBC Radio Derby (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioDevon_HLS, title='Play BBC Radio Devon (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioEssex_HLS, title='Play BBC Radio Essex (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioGloucestershire_HLS, title='Play BBC Radio Gloucestershire (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioGuernsey_HLS, title='Play BBC Radio Guernsey (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioHerefordWorcester_HLS, title='Play BBC Radio Hereford Worcester (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioHumberside_HLS, title='Play BBC Radio Humberside (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioJersey_HLS, title='Play BBC Radio Jersey (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioKent_HLS, title='Play BBC Radio Kent (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioLancashire_HLS, title='Play BBC Radio Lancashire (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioLeeds_HLS, title='Play BBC Radio Leeds (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioLeicester_HLS, title='Play BBC Radio Leicester (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioLincolnshire_HLS, title='Play BBC Radio Lincolnshire (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioLondon_HLS, title='Play BBC Radio London (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioManchester_HLS, title='Play BBC Radio Manchester (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioMerseyside_HLS, title='Play BBC Radio Merseyside (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioNewcastle_HLS, title='Play BBC Radio Newcastle (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioNorfolk_HLS, title='Play BBC Radio Norfolk (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioNorthampton_HLS, title='Play BBC Radio Northampton (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioNottingham_HLS, title='Play BBC Radio Nottingham (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioOxford_HLS, title='Play BBC Radio Oxford (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioSheffield_HLS, title='Play BBC Radio Sheffield (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioShropshire_HLS, title='Play BBC Radio Shropshire (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioSolent_HLS, title='Play BBC Radio Solent (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioSomerset_HLS, title='Play BBC Radio Somerset Sound (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioStoke_HLS, title='Play BBC Radio Stoke (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioSuffolk_HLS, title='Play BBC Radio Suffolk (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioSurrey_HLS, title='Play BBC Radio Surrey (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioSussex_HLS, title='Play BBC Radio Sussex (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioTees_HLS, title='Play BBC Radio Tees (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=Radio3Counties_HLS, title='Play BBC Radio Three Counties (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioWiltshire_HLS, title='Play BBC Radio Wiltshire (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioWestMidlands_HLS, title='Play BBC Radio West Midlands (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioYork_HLS, title='Play BBC Radio York (HLS)', fmt='hls'))
    oc.add(CreateTrackObject(url=RadioWorldService_HLS, title='Play BBC World Service (HLS)', fmt='hls'))
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
    elif fmt == 'hls':
        protocol = 'hls'
        container = 'mpegts'
        # video_codec = VideoCodec.H264
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
