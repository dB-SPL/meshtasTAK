# meshtasTAK

This is a quick-and-dirty script for capturing position reports and messages from LoRa nodes on a Meshtastic network and sending them as Cursor-on-Target (CoT) messages to a TAK server such as FreeTakServer for display on connected clients such as phones running the Android Team Awareness Kit (ATAK).

It requires a USB connection between the Meshtastic device and the device running the script as well as a TCP/IP network connection to the TAK server.  The script uses the Meshtastic-Python API to communicate with the Meshtastic radio.

## Installation
To install the module, use:

python -m pip install https://github.com/DeltaBravo15/meshtasTAK/archive/master.zip

The installation process should also install the lastest version of takpak to create and read CoT messages.  If you have problems with the installation process, please let me know.

For now, you'll also need to edit '__main__.py' to point to the IP address of your TAK sever.  This should be more easily configurable soon

## Launching the Module

It's my goal for future versions to support full interoperabilty between Meshtastic devices and TAK servers and clients.  It's also my hope that someone might be inspired to implement similar functionality in an a smartphone app that would allow TAK clients to directly communicate over a mesh network of Meshtastic devices.

I'd love to hear your feedback on the ATAK Discord at https://discordapp.com/invite/XEPyhHA or the ATAK subreddit at https://www.reddit.com/r/ATAK/

For more information, please visit:

Meshtastic https://www.meshtastic.org/

Meshtastic-Python https://github.com/meshtastic/Meshtastic-Python

Free TAKServer https://github.com/FreeTAKTeam/FreeTAKServer

takpak https://github.com/pinztrek/takpak
