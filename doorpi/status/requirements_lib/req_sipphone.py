#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)
logger.debug("%s loaded", __name__)

from doorpi.sipphone.AbstractBaseClass import SIPPHONE_SECTION

REQUIREMENT = dict(
    fulfilled_with_one = True,
    text_description = 'The task of a SIP Phone within DoorPi is to make the telephone calls (VoIP connections). In addition the Sip-Phone can work either with or without a SIP server (for example Fritz box or Asterisk) together.',
    events = [
        dict( name = 'OnSipPhoneCreate', description = 'The SIP Phone has been created and can be started.'),
        dict( name = 'OnSipPhoneStart', description = 'The SIP Phone was started and is now ready for use.'),
        dict( name = 'OnSipPhoneDestroy', description = 'The SIP phone will be terminated.'),
        dict( name = 'OnSipPhoneRecorderCreate', description = 'Recorder has been created and is now ready to record calls.'),
        dict( name = 'OnSipPhoneRecorderDestroy', description = 'A recorder has been stopped and no further recordings are possible'),
        dict( name = 'BeforeSipPhoneMakeCall', description = 'A call is about to be started from DoorPi.'),
        dict( name = 'OnSipPhoneMakeCall', description = 'A call is started from DoorPi.'),
        dict( name = 'OnSipPhoneMakeCallFailed', description = 'An error has occurred when attempting to make a call from DoorPi.'),
        dict( name = 'AfterSipPhoneMakeCall', description = 'The call was made and the phone is ringing at the remote station'),
        dict( name = 'OnSipPhoneCallTimeoutNoResponse', description = 'The call was ended because the remote station has not answered (parameter call_timeout)'),
        dict( name = 'OnSipPhoneCallTimeoutMaxCalltime', description = 'The call was ended because the call was running for longer than allowed (parameter max_call_time)'),
        dict( name = 'OnPlayerCreated', description = 'A player has been created and it will be possible to play a sound file as a waiting music at the next call (parameter dialtone)'),
        dict( name = 'OnCallMediaStateChange', description = 'The use of the input and output devices (audio and video) has changed.'),
        dict( name = 'OnMediaRequired', description = 'There is a call and the media device is needed. Can e.g. be used to activate amplifiers.'),
        dict( name = 'OnMediaNotRequired', description = 'There is no call and the media device is not needed anymore. Can e.g. be used to disable amplifier.'),
        dict( name = 'OnCallStateChange', description = 'The status of a call has changed'),
        dict( name = 'OnCallStateConnect', description = 'The call is now connected again (Connected, Resuming or Updating)'),
        dict( name = 'AfterCallStateConnect', description = 'The conversation has been established, the media connection exists'),
        dict( name = 'OnCallStateDisconnect', description = 'The conversation has ended'),
        dict( name = 'AfterCallStateDisconnect', description = '[not used anymore]'),
        dict( name = 'OnCallStateDismissed', description = 'The call was dismissed due to the remote station being busy.'),
        dict( name = 'OnCallStateReject', description = 'The call was rejected by the other party.'),
        dict( name = 'OnCallStart', description = 'Initialization of call-back functions'),
        dict( name = 'OnDTMF', description = 'DTMF signals were received. In addition, an event in the form ´OnDTMF_"#"´ is triggered (if # was pressed) if the received DTMF signal was defined in the Config and thus expected.'),
        dict( name = 'BeforeCallIncoming', description = 'A call has arrived and has not been processed yet'),
        dict( name = 'OnCallReconnect', description = 'If a call already exists and a call is rebuilt to the same number.'),
        dict( name = 'AfterCallReconnect', description = 'After a conversation has already existed and a call for the same number has been rebuilt.'),
        dict( name = 'OnCallBusy', description = 'DoorPi is currently busy and can not accept another call.'),
        dict( name = 'AfterCallBusy', description = 'After DoorPi has rejected an incoming call, as already another conversation is conducted.'),
        dict( name = 'OnCallIncoming', description = 'Before an incoming call is accepted (is an admin number)'),
        dict( name = 'AfterCallIncoming', description = 'After an incoming call has been accepted (is an admin number)'),
        dict( name = 'OnCallReject', description = 'Before an incoming call is rejected (no admin number)'),
        dict( name = 'AfterCallReject', description = 'After an incoming call has been rejected (no admin number)'),
        dict( name = 'OnPlayerStarted', description = 'The playback of the DialTone has started'),
        dict( name = 'OnPlayerStopped', description = 'The playback of the DialTone has stopped),
        dict( name = 'OnRecorderStarted', description = 'The recording of the conversation has started'),
        dict( name = 'OnRecorderStopped', description = 'The recording of the conversation has stopped'),
        dict( name = 'OnRecorderCreated', description = 'Recorder has been created a recorder and is ready to record calls.')
    ],
    configuration = [
        dict( section = SIPPHONE_SECTION, key = 'sipphonetyp', type = 'string', default = '', mandatory = False, description = 'Select which SIP phone to use ("linphone" or "pjsua")'),
        dict( section = SIPPHONE_SECTION, key = 'sipphone_server', type = 'string', default = '', mandatory = False, description = 'If a SIP-Phone server is to be used, the server, the user name, the password and the realm must be specified.'),
        dict( section = SIPPHONE_SECTION, key = 'sipphone_username', type = 'string', default = '', mandatory = False, description = 'User to log in to the SIP Phone Server'),
        dict( section = SIPPHONE_SECTION, key = 'sipphone_password', type = 'string', default = '', mandatory = False, description = 'Password to log in to the SIP Phone Server'),
        dict( section = SIPPHONE_SECTION, key = 'sipphone_realm', type = 'string', default = '', mandatory = False, description = 'Realm for logging on to the SIP Phone Server (for example, "fritz.box" in the FritzBox)'),
        dict( section = SIPPHONE_SECTION, key = 'identity', type = 'string', default = 'DoorPi', mandatory = False, description = 'Name displayed on the phone conversation '),
        dict( section = SIPPHONE_SECTION, key = 'ua.max_calls', type = 'integer', default = '2', mandatory = False, description = 'Number of max. simultaneous conversations'),
        dict( section = SIPPHONE_SECTION, key = 'local_port', type = 'integer', default = '5060', mandatory = False, description = 'The port to be accepted on the VoIP SIP calls.'),
        dict( section = SIPPHONE_SECTION, key = 'max_call_time', type = 'integer', default = '120', mandatory = False, description = 'maximum time of a conversation until automatic hang up'),
        dict( section = SIPPHONE_SECTION, key = 'call_timeout', type = 'integer', default = '15', mandatory = False, description = 'maximum time for DoorPi to ring the phone before it hangs up again'),
        dict( section = SIPPHONE_SECTION, key = 'dialtone', type = 'string', default = '', mandatory = False, description = 'Path to the DialTone file. this is played when a bell is pressed and serves as a sign that it is ringing for the visitor. (for example! BASEPATH! /doorpi/media/ShortDialTone.wav)'),
        dict( section = SIPPHONE_SECTION, key = 'dialtone_renew_every_start', type = 'boolean', default = '', mandatory = False, description = 'The DialTone should be created again at every start.'),
        dict( section = SIPPHONE_SECTION, key = 'dialtone_volume', type = 'integer', default = '35', mandatory = False, description = 'Volume of the dial tone to be generated (in%).'),
        dict( section = SIPPHONE_SECTION, key = 'records', type = 'string', default = '', mandatory = False, description = 'Storage path of recorded calls (e.g. !BASEPATH!/records/!LastKey!/%Y-%m-%d_%H-%M-%S.wav)'),
        dict( section = SIPPHONE_SECTION, key = 'record_while_dialing', type = 'string', default = 'False', mandatory = False, description = 'Should the conversation already be recorded when it rings (True) or only when the other side has taken away (False). In case of missed calls you may be able to recognize the visitor due to the noise.'),
        dict( section = SIPPHONE_SECTION, key = 'snapshot_path', type = 'string', default = '!Basepath!/doorpi/media/snapshots', mandatory = False, description = 'Storage path of created images before ringing (e.g. !BASEPATH!/doorpi/media/snapshots)'),
        dict( section = SIPPHONE_SECTION, key = 'number_of_snapshots', type = 'integer', default = '10', mandatory = False, description = 'Number of pictures saved.')
    ],
    libraries = dict(
        linphone = dict(
            text_description =      '''
Linphone is a free IP telephony (VoIP) software available under the GNU GPLv2 license. It is a simple and reliable VoIP program with video transmission. Because of the very good video quality, it is also suitable for conversations in sign language, for example.

The program is available in a Linux, Windows and OS-X version, for unix-like operating systems such as FreeBSD the freely accessible source code can be used. There are also clients for Android, iOS, Blackberry and Windows Phone. In addition to the GTK + -based graphical interface, there are also two console programs.

The program has the following functions:
<ul>
<li> Internet telephony - based on the SIP standard </li>
<li> Videophone or Videoconference </li>
<li> presence (you can tell if a conversation is currently available) </li>
<li> Instant Messaging </li>
<li> Encryption of audio and video transmission </li>
</ul>

The following codecs are available for voice transmission:
<ul>
<li>G.711a or G.711u</li>
<li>GSM</li>
<li>Speex</li>
<li>LPC10-15</li>
<li>G.722</li>
<li>Opus</li>
</ul>

Video transmissions can be made using the following codecs:
<ul>
<li>H.263 or H.263+</li>
<li>MPEG4 Part 2</li>
<li>Theora</li>
<li>H.264 (with plug-in based on x264)</li>
</ul>

Encryption can be done with the following protocols:
<ul>
SRTP
ZRTP
</ul>
The STUN protocol is available for operation behind a NAT router.''',
            text_installation =     'The installation is very good <a href="https://wiki.linphone.org/wiki/index.php/Raspberrypi:start">in the wiki of linphone</a> described.</br>',
            auto_install =          True,
            text_test = 'You can manually test the status at any time by entering <code> import linphone </code> in the Python interpreter.',
            text_configuration = 'There are a variety of parameters available for configuring Linphone, which can be found in the <a href="http://192.168.1.214/dashboard/pages/config.html"> Configuration </a> can be viewed.',
            configuration = [
                dict( section = SIPPHONE_SECTION, key = 'echo_cancellation_enabled', type = 'boolean', default = 'False', mandatory = False, description = 'Software-based echo suppression - Attention: very high system utilization and not recommended'),
                dict( section = SIPPHONE_SECTION, key = 'video_display_enabled', type = 'boolean', default = 'False', mandatory = False, description = 'Should a video be displayed in the field? - Attention: very high system utilization and not recommended'),
                dict( section = SIPPHONE_SECTION, key = 'stun_server', type = 'string', default = '', mandatory = False, description = 'STUN server to be used'),
                dict( section = SIPPHONE_SECTION, key = 'FirewallPolicy', type = 'string', default = 'PolicyNoFirewall', mandatory = False, description = 'Possible values: PolicyNoFirewall, PolicyUseStun, PolicyUseIce and PolicyUseUpnp.'),
                dict( section = SIPPHONE_SECTION, key = 'video_device', type = 'string', default = '', mandatory = False, description = 'Camera used for recording - if nothing is specified then the best one will be used. Please search for "possible videodevices:" in the LOG file'),
                dict( section = SIPPHONE_SECTION, key = 'video_size', type = 'string', default = '', mandatory = False, description = 'possible values: [missing]'),
                dict( section = SIPPHONE_SECTION, key = 'video_codecs', type = 'array', default = 'VP8', mandatory = False, description = 'Video codecs that can be activated and used.'),
                dict( section = SIPPHONE_SECTION, key = 'capture_device', type = 'string', default = '', mandatory = False, description = 'Audio device that is used for recording - if nothing is specified, then the best is used. Please search for "possible sounddevices:" in the LOG file'),
                dict( section = SIPPHONE_SECTION, key = 'mic_gain_db', type = 'float', default = '0', mandatory = False, description = 'Additional software amplification of the recording if the level of the microphone is too weak, even at maximum mixer setting.'),
                dict( section = SIPPHONE_SECTION, key = 'playback_device', type = 'string', default = '', mandatory = False, description = 'Audio device that is used for recording - if nothing is specified, then the best is used. Please search for "possible sounddevices:" in the LOG file'),
                dict( section = SIPPHONE_SECTION, key = 'audio_codecs', type = 'array', default = 'PCMA,PCMU', mandatory = False, description = 'Audio codecs that can be activated and used.'),
            ],
            text_links = {
                'linphone.org': {
                    'Overview Liblinphone': 'http://www.linphone.org/technical-corner/liblinphone/overview',
                    'Installation instructions in the wiki': 'https://wiki.linphone.org/wiki/index.php/Raspberrypi:start',
                    'News Linphone für Raspberry': 'http://www.linphone.org/news/32/26/Linphone-Python-for-Raspberry-Pi-3-8.html'
                },
                'Linphone for Python documentation': 'http://pythonhosted.org/linphone/',
                'linphone on wikipedia.de': 'https://de.wikipedia.org/wiki/Linphone'
            }
        ),
        pjsua = dict(
            text_warning =          'The SIP Phone pjsua is currently no longer supported in the DoorPi project. It is highly recommended to switch to <a href="{BASE_URL}/help/modules.overview.html?module=sipphone&name=linphone"> linphone </a>.',
            text_description =      '',
            text_installation =     '',
            text_test =             'The status can be tested by entering <code> import {MODULE_NAME} </ code> in the Python interpreter.',
            text_configuration =    '',
            configuration = [],
            text_links = {
                'Homepage Pjsua': 'http://www.pjsip.org/pjsua.htm',
                'Installation Instructions PJSIP ': 'http://trac.pjsip.org/repos/wiki/Getting-Started'
            }
        )
    )
)

