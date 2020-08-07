This is a quick and dirty script for capturing position reports and messages from LoRa nodes on a Meshtastic network and sending them as Cursor-on-Target (CoT) messages to a TAK server such as FreeTakServer for display on connected clients such as phones running the Android Team Awareness Kit (ATAK).

It requires a USB connection between the Meshtastic device and the device running the script as well as a TCP/IP network connection to the TAK server.

This script requires (and is only possible because of) the takpak Python library for creating and sending CoT messages.  Some of the files from that library have temporarily been included in this repository as I hard-coded some changes into them.  As the code is cleaned up, this script will be able to use the takpak library as-is, and those files will be removed.
