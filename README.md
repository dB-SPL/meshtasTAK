# meshtasTAK
Recently, the Meshtastic project has released their own plugin for ATAK, which may be more useful to you than this script that is no longer maintained.  You can find the official ATAK plugin from the Meshtastic project at:
https://github.com/meshtastic/ATAK-Plugin

## About
This is a quick-and-dirty script for capturing position reports and messages from LoRa nodes on a Meshtastic network and sending them as Cursor-on-Target (CoT) messages to a TAK server such as FreeTakServer for display on connected clients such as phones running the Android Team Awareness Kit (ATAK).

It requires a USB connection between the Meshtastic device and the device running the script as well as a TCP/IP network connection to the TAK server. The script uses the Meshtastic-Python API to communicate with the Meshtastic radio.

## Installation
To install the module, use:

`pip install https://github.com/DeltaBravo15/meshtasTAK/archive/master.zip`

The installation process should also install the lastest version of takpak to create and read CoT messages. If you have problems with the installation process, please let me know.

## Launching the Module
`python -m mestasTAK <TAKServer_IP> <TAKServer_Port>`

You may optionally specify a TAK server IP address and port number. If not, the module will attempt to connect to the localhost on port 8087.

It's my goal for future versions to support full interoperabilty between Meshtastic devices and TAK servers and clients. It's also my hope that someone might be inspired to implement similar functionality in an a smartphone app that would allow TAK clients to directly communicate over a mesh network of Meshtastic devices.

I'd love to hear your feedback on the ATAK Discord at https://discordapp.com/invite/XEPyhHA or the ATAK subreddit at https://www.reddit.com/r/ATAK/

## For more information, please visit:
Meshtastic https://www.meshtastic.org/

Meshtastic-Python https://github.com/meshtastic/Meshtastic-Python

Free TAKServer https://github.com/FreeTAKTeam/FreeTAKServer

takpak https://github.com/pinztrek/takpak
