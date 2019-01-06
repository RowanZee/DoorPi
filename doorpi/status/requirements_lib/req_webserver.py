#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)
logger.debug("%s loaded", __name__)

from doorpi.status.webserver import DOORPIWEB_SECTION, CONF_AREA_PREFIX

REQUIREMENT = dict(
    fulfilled_with_one = False,
    text_description = '''The web server is the control and configuration interface as well as the interface via web service.
Files can be requested (eg index.html) which are loaded from the file system (real resources).
But it is also possible to process status queries or control commands (virtual resources).

The user will primarily call only real resources that "reload" the displayed status via virtual resources.

If it comes to a web interface, then this should also be secured.
There are users (users) that are grouped in groups.
These groups are assigned areas (AREA) that can be used for reading or writing.
The areas (AREA) are virtual and real resources that differ specifically in the URL (hence the idea to divide it into areas).
The components of an area are defined by RegEx.

Assignment in the User section is:
[Username] = [password]

At the group section it is:
[GroupName] = [username1], [username2], [...]

Then there are the two sections WritePermission and ReadPermission with the assignment:
[GroupName] = [AreaName]

At the bottom there are any number of areas with different names. Each area is assigned RegEx, which are checked against the URL.
A special form is the AREA_public. It summarizes all the resources that anyone can view, since they are Javascript, CSS and similar files.
This was necessary because the login.html had also loaded Javascript files. Mitlerweile I have adopted by the login.html einw enig and I have gone towards HTTP status code 401 with base64 coded password. This can also be done automatically later, so that web service actions with authentication are possible on a very simple standardized level.

Example
<code>
['''+DOORPIWEB_SECTION+''']
public = AREA_public # These are all resources that anyone can see, even if they have not authenticated themselves

[User]
door = pi # User door with the password pi

[Group]
administrator = door # User door is a member of the group administrator

[WritePermission]
administrator = dashboard # Group administrator can write access to the resources dashboard (Section "'''+CONF_AREA_PREFIX+'''dashboard")

[ReadPermission]
administrator = status, help # Group administrator is allowed to read the resource status (Section "'''+CONF_AREA_PREFIX+'''status") and help (Section "'''+CONF_AREA_PREFIX+'''help") access

['''+CONF_AREA_PREFIX+'''status]
/status # all URLs that match "/status" (Parameters of the URL do not matter - for example, "/status?output=plain")
/mirror

['''+CONF_AREA_PREFIX+'''dashboard]
/dashboard/pages/.*html

['''+CONF_AREA_PREFIX+'''help]
/help/.*

['''+CONF_AREA_PREFIX+'''public]
/dashboard/bower_components/.*
/dashboard/dist/.*
/dashboard/js/.*
/dashboard/less/.*
/login.html
/favicon.ico
</code>
''',
    events = [
        dict( name = 'OnWebServerStart', description = 'The web server is started, so the web services and the web interface are available By default, port 80 is used (Parameter ip and port)'),
        dict( name = 'OnWebServerStop', description = 'The web server should be stopped, from this point on no new requests will be processed.'),
        dict( name = 'WebServerCreateNewSession', description = 'A user who has logged in since the start of DoorPi has logged in.'),
        dict( name = 'WebServerAuthUnknownUser', description = 'An attempt was made to log in with a user who is not known.'),
        dict( name = 'WebServerAuthWrongPassword', description = 'An incorrect password was sent for an existing user.'),
        dict( name = 'OnWebServerRequest', description = 'A request has been made to the web server - whether by GET or POST'),
        dict( name = 'OnWebServerRequestGet', description = 'A GET request was made to the web server'),
        dict( name = 'OnWebServerRequestPost', description = 'A POST request has been made to the web server'),
        dict( name = 'OnWebServerVirtualResource', description = 'A request has been made to the web server pointing to a virtual resource (e.g., webservice requires JSON string)'),
        dict( name = 'OnWebServerRealResource', description = 'A request has been made to the web server pointing to a real resource (e.g., user is calling the dashboard)'),
    ],
    configuration = [
        dict( section = DOORPIWEB_SECTION, key = 'ip', type = 'string', default = '', mandatory = False, description = 'IP address to which the web server is to be bound (empty = all)'),
        dict( section = DOORPIWEB_SECTION, key = 'port', type = 'integer', default = '80', mandatory = False, description = 'The port on which the web server should listen. Attention - can lead to collisions with other installed web servers!'),
        dict( section = DOORPIWEB_SECTION, key = 'www', type = 'string', default = '!BASEPATH!/../DoorPiWeb', mandatory = False, description = 'Location of the files to be used for real resources. If these are not found, the online fallback is automatically used.'),
        dict( section = DOORPIWEB_SECTION, key = 'indexfile', type = 'string', default = 'index.html', mandatory = False, description = '[not involved]'),
        dict( section = DOORPIWEB_SECTION, key = 'loginfile', type = 'string', default = 'login.html', mandatory = False, description = 'Attention: outdated! The name of the login file to be displayed if there is no valid authentication.'),
        dict( section = DOORPIWEB_SECTION, key = 'public', type = 'string', default = 'AREA_public', mandatory = False, description = 'The name of the Public section with all publicly invokable resources (for example JS and CSS files for the Dashbaord)'),
        dict( section = DOORPIWEB_SECTION, key = 'online_fallback', type = 'string', default = 'http://RowanZee.github.io/DoorPiWeb', mandatory = False, description = 'The address for the online fallback - from here the data are loaded if they were not found locally.'),
        dict( section = 'User', key = '*', type = 'string', default = '', mandatory = False, description = 'Section that includes all users - in the form [username] = [password]'),
        dict( section = 'Group', key = '*', type = 'string', default = '', mandatory = False, description = 'Section that includes all groups and their members. Several users are separated by a comma - in the form [groupname] = [user1], [user2], ...'),
        dict( section = 'ReadPermission', key = '*', type = 'string', default = '', mandatory = False, description = ''),
        dict( section = 'WritePermission', key = '*', type = 'string', default = '', mandatory = False, description = ''),
        dict( section = CONF_AREA_PREFIX+'*', key = '*', type = 'string', default = '', mandatory = False, description = '')
    ],
    libraries = dict(
        BaseHTTPServer = dict(
            text_warning =          '',
            text_description =      'The Python module BaseHTTPServer with the class HTTPServer is the basis for every web server.',
            text_installation =     'An installation is not necessary as this is a Python standard module.',
            auto_install =          False,
            text_test =             'The status can be tested by entering <code> import BaseHTTPServer </code> in the Python interpreter.',
            text_configuration =    '',
            configuration = [
                #dict( section = 'DoorPi', key = 'eventlog', type = 'string', default = '!BASEPATH!/conf/eventlog.db', mandatory = False, description = 'Location of the SQLLite database for the event handler.')
            ],
            text_links = {
                'docs.python.org': 'https://docs.python.org/2.7/library/basehttpserver.html'
            }
        ),
        SocketServer = dict(
            text_warning =          '',
            text_description =      'The Python module SocketServer provides the class ThreadingMixIn, with the help of which the web server can receive and process several requests at the same time.',
            text_installation =     'An installation is not necessary as this is a Python standard module.',
            auto_install =          False,
            text_test =             'The status can be tested by entering <code> import SocketServer </code> in the Python interpreter.',
            text_configuration =    '',
            configuration = [
                #dict( section = 'DoorPi', key = 'eventlog', type = 'string', default = '!BASEPATH!/conf/eventlog.db', mandatory = False, description = 'Location of the SQLLite database for the event handler.')
            ],
            text_links = {
                'docs.python.org': 'https://docs.python.org/2.7/library/socketserver.html'
            }
        ),
        urlparse = dict(
            text_warning =          '',
            text_description =      'The python module urlparse provides the two functions urlparse and parse_qs, with the help of which the parameters of a web server request can be split and processed.',
            text_installation =     'An installation is not necessary as this is a Python standard module.',
            auto_install =          False,
            text_test =             'The status can be tested by entering <code> import urlparse </code> in the Python interpreter.',
            text_configuration =    '',
            configuration = [
                #dict( section = 'DoorPi', key = 'eventlog', type = 'string', default = '!BASEPATH!/conf/eventlog.db', mandatory = False, description = 'Location of the SQLLite database for the event handler.')
            ],
            text_links = {
                'docs.python.org': 'https://docs.python.org/2.7/library/urlparse.html'
            }
        ),
        urllib2 = dict(
            text_warning =          '',
            text_description =      'The python module urllib2 makes it possible to submit requests to a web server. In DoorPi, this is done on the one hand when testing the own web server (fake_request) and on the other hand when loading sources from the online fallback (load_online_fallback).',
            text_installation =     'An installation is not necessary as this is a Python standard module.',
            auto_install =          False,
            text_test =             'The status can be tested by entering <code> import BaseHTTPServer </code> in the Python interpreter.',
            text_configuration =    '',
            configuration = [
                #dict( section = 'DoorPi', key = 'eventlog', type = 'string', default = '!BASEPATH!/conf/eventlog.db', mandatory = False, description = 'Location of the SQLLite database for the event handler.')
            ],
            text_links = {
                'docs.python.org': 'https://docs.python.org/2.7/library/urllib2.html'
            }
        ),
        mimetypes = dict(
            text_warning =          '',
            text_description =      'The Python module mimetypes allows the determination of the MIME type based on file extensions. The important thing is that when deciding to place wildcards within this file should be processed (HTML template) or not (for example, image file).',
            text_installation =     'An installation is not necessary as this is a Python standard module.',
            auto_install =          False,
            text_test =             'The status can be tested by entering <code> import BaseHTTPServer </code> in the Python interpreter.',
            text_configuration =    '',
            configuration = [
                #dict( section = 'DoorPi', key = 'eventlog', type = 'string', default = '!BASEPATH!/conf/eventlog.db', mandatory = False, description = 'Location of the SQLLite database for the event handler.')
            ],
            text_links = {
                'docs.python.org': 'https://docs.python.org/2.7/library/mimetypes.html',
                'MIME-Typen': 'http://wiki.selfhtml.org/wiki/Referenz:MIME-Typen',
                'Media Types on iana.org': 'http://www.iana.org/assignments/media-types/media-types.xhtml',
                'RFC2616  - Section 14.17': 'https://tools.ietf.org/html/rfc2616#section-14.17'
            }
        )
    )
)

