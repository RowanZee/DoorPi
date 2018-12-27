****************************************************
DoorPi: Open Source VoIP Door Phone
****************************************************

|pypi_License| |pypi_latest_version| |travis_status_master| |code_climate_badge| |scrutinizer_status_master|

.. contents::
    :local:
    :depth: 2
    :backlinks: none

---------------
Introduction
---------------
The goal of the project DoorPi is to control a door intercom by means of a single-board computer such as the Raspberry Pi and the communication protocol VoIP.

DoorPi is an event-action based system. There are components that trigger events and components that respond because of these events. For this purpose, events such as "pressing a doorbell" or "RFID Chip xyz held" triggers actions (Actions) such as "call on phone xyz", "e-mail to xxx" or "open door".
---------------
Event Sources
---------------

To register these events, "DoorPi keyboards" are used, which, for example:

* The GPIO pins
* A PiFace
* Files in the file system of the Pi (for example, for remote commands via SSH)
* The serial interface (RDM6300 as NFC reader)
* Web service with authentication
* VoIP phone

Any number of actions that are executed synchronously or asynchronously can be added to any event.

-----------------
Action-Receivers
-----------------

A non-complete list of actions is:

* VOIP call to a predefined number
* VOIP call to a number which is read from a file
* end call
* send email
* execute program
* set an output pin
* write a status file
* read values from IP-Symcon or write them back
* ...

Via the combination of events and actions, almost all combinations are possible.


-----------------
Examples
-----------------

One possible scenario is:

#. When pressing a bell push a call is triggered and specifically called a number (for example, internal FritzBox number \ * \ * 613 but also mobile phone numbers).
#. The resident can make calls to the field office and, if desired, open the door remotely by pressing a defined key (or key sequence) on the telephone (e.g., the "#" key).
#. The resident forgets to hang up and DoorPi himself ends the call as soon as the door is closed again.
#. DoorPi sends an e-mail saying there was a phone call, someone opened the door and someone walked into the house.

Meanwhile, there is also video support so that a camera can be installed on the front door and the image can be viewed on the indoor stations, even before the call is accepted.

-----------------
Installation
-----------------

The installation is described here `http://www.doorpi.org/forum/board/21-installation/>` (German thread)

-----------------
DoorPi-Help 
-----------------

Link to forums with DoorPi articles (German articles):

`DoorPi Forum <http://www.doorpi.org/forum/>`_

`[Home Care] DoorPi (VoIP Intercom / Door phone with Video-Support) <http://www.forum-raspberrypi.de/Thread-haussteuerung-doorpi-voip-wechselsprechanlage-tuersprechanlage-mit-video-support>`_

`DoorPI / VoIP Door-Intercom with Raspberry Pi <http://www.ip-symcon.de/forum/threads/26739-DoorPI-VoIP-Door-Intercomstation-with-Raspberry-Pi>`_
