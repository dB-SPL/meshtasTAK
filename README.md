meshtasTAK

This is a quick-and-dirty script for capturing position reports and messages from LoRa nodes on a Meshtastic network and sending them as Cursor-on-Target (CoT) messages to a TAK server such as FreeTakServer for display on connected clients such as phones running the Android Team Awareness Kit (ATAK).

It requires a USB connection between the Meshtastic device and the device running the script as well as a TCP/IP network connection to the TAK server.  The script uses the Meshtastic-Python API to communicate with the Meshtastic radio.

This script requires (and is only possible because of) the takpak Python library for creating and sending CoT messages.  Some of the files from that library have temporarily been included in this repository as I hard-coded some changes into them.  As the code is cleaned up, this script will be made directly compatible with the takpak library, and those files will be removed.

At present, the script assumes all of the necessary modules are installed.  There is not yet any checking for requirments or a means for automated installation.

It's my goal to create a Python module for full interoperabilty between Meshtastic devices and TAK servers and clients.  It's also my hope that someone might be inspired to implement similar functionality in an a smartphone app that would allow TAK clients to directly communicate over a mesh network of Meshtastic devices.

I'd love to hear your feedback on the ATAK Discord at https://discordapp.com/invite/XEPyhHA or the ATAK subreddit at https://www.reddit.com/r/ATAK/

For more information, please visit:
Meshtastic https://www.meshtastic.org/
Meshtastic-Python https://github.com/meshtastic/Meshtastic-Python
Free TAKServer https://github.com/FreeTAKTeam/FreeTAKServer
takpak https://github.com/pinztrek/takpak
