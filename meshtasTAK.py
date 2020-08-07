import time
#from time import sleep,gmtime,strftime
import os
import uuid
#from socket import getfqdn
import socket 

#import takcot. Note this only works if you have installed the package
#   If you have not installed as a package, you may have to tune your imports
#   to be local to where your source is

from takpak.takcot import takcot
from takpak.mkcot import mkcot

#import meshtastic
import meshtastic
from pubsub import pub

def timestamp():
    timeString = time.strftime("%H:%M:%S", time.localtime())
    return timeString

def onNodeUpdate(node):
    print(f"{timestamp()} {node}")
    print()

def onReceive(packet): # called when a packet arrives
	packetType = list(packet['decoded'].keys())[0]
	print(f"{timestamp()} {packet}") # prints incoming packet to STDOUT
	if packetType == 'user':
	    meshId = packet['from']
	    meshUserId = packet['decoded']['user']['id']
	    meshLongName = packet['decoded']['user']['longName']
	    cotId = meshLongName + "-" + str(uuid.uuid1())[-12:]
	    users.update({meshId : {'meshUserId' : meshUserId, 'meshLongName' : meshLongName, 'cotId' : cotId}})
	    print(f"Received User Packet from {meshLongName}")
	    print(f"Current Users: {users}")
	    print()
	if packetType == 'position':
	    meshId = packet['from']
	    if meshId in users:
	        meshLongName = users[meshId]['meshLongName']
	    else:
	        meshLongName = packet['from']
	    print(f"Received Position Packet from {meshLongName}")
	    if 'latitude' in packet['decoded']['position']:
	        lat = packet['decoded']['position']['latitude']
	        lon = packet['decoded']['position']['longitude']
	        if lon < 0:
	            lon = -lon
	        alt = packet['decoded']['position']['altitude']
	        cotId = users[meshId]['cotId']
	        print(f"Lat: {lat} Lon: {lon} Alt: {alt}")
	        takserver.taksend(mkcot.mkcot(cot_identity="friend"
	            , cot_stale = 10
	            , cot_dimension="land-unit",cot_typesuffix="E-C-T"
	            , cot_lat=lat, cot_lon=-lon, cot_hae=alt
	            , cot_id=cotId
				, cot_callsign=meshLongName))
	        time.sleep(1)
	        print("read the response")
	    print()
	if packetType == 'data':
	    meshId = packet['from']
	    if meshId in users:
	        meshLongName = users[meshId]['meshLongName']
	    else:
	        meshLongName = packet['from']
	    print(f"Received Data Packet from {meshLongName}")
	    print()

#logging.basicConfig(level=logging.INFO) # level=10

sleeptime = 0.075

TAK_IP = '192.168.10.130'
#TAK_IP = '204.48.30.216'
TAK_PORT = 8087

#TAK_IP = os.getenv('ATAK_IP', '204.48.30.216')
#TAK_PORT = int(os.getenv('ATAK_PORT', '8087'))

#-----------------------------------------------------------------------------------------


# substantiate the class
takserver = takcot()

# Now open server
print("Opening TAK Server")
testsock = takserver.takopen(TAK_IP)

print("open return is:")
print(testsock)

#connect_xml=cot_xml
print()
print("send a connect")
takserver.takflush()  # flush the xmls the server sends
print(takserver.takread())  # read all the server CoT's, will send last + the connct

# send the connect string, server does not echo
takserver.taksend(mkcot.mkcot(cot_type="t", cot_how="h-g-i-g-o")) 

print("read the Connect response")
print(takserver.takread())  # read all the server CoT's, will send last + the connct

#print("Flush the server response")
takserver.takflush()  # flush the xmls the server sends
time.sleep(1)

users = {}
time.sleep(100)
interface = meshtastic.StreamInterface()
pub.subscribe(onNodeUpdate, "meshtastic.node.updated")
pub.subscribe(onReceive, "meshtastic.receive")

# Always need to close out the connection
# good practice to include reading anything the server pushed
# to prevent broken pipe errors on the server

#takserver.takflush()  # flush the xmls the server sends

#print("Closing TAK Server")
#takserver.takclose()
