import time
#from time import sleep,gmtime,strftime
import os
import uuid
#from socket import getfqdn
import socket 
from threading import Thread

#import takcot. Note this only works if you have installed the package
#   If you have not installed as a package, you may have to tune your imports
#   to be local to where your source is

from takpak.takcot import takcot
from takpak.mkcot import mkcot

#import meshtastic
import meshtastic
from pubsub import pub

sleeptime = 0.075

TAK_IP = sys.argv[1]
TAK_PORT = sys.argv[2]

#TAK_IP = os.getenv('ATAK_IP', '204.48.30.216')
#TAK_PORT = int(os.getenv('ATAK_PORT', '8087'))

def timestamp():
    timeString = time.strftime("%H:%M:%S", time.localtime())
    return timeString

def ping():
	print("send ping")
	takserver.send(mkcot.mkcot(cot_id = my_uid + "-ping",cot_type="t-x-c-t"))
	print("read the ping response")
	print(takserver.read())
	print()

def pingTimer():
	time.sleep(30)
	ping()

def onNodeUpdate(node):
    print(f"{timestamp()} {node}")
    print()
	
def onReceive(packet): # called when a packet arrives
	packetType = list(packet['decoded'].keys())[0]
	#print(f"{timestamp() packet}") # prints incoming packet to STDOUT
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
			print(f"Received Position Packet from {meshLongName}")
			if 'latitude' in packet['decoded']['position'] and 'longitude' in packet['decoded']['position']:
				lat = packet['decoded']['position']['latitude']
				lon = packet['decoded']['position']['longitude']
				if lon < 0:
					lon = -lon
				alt = 0
				if 'altitude' in packet['decoded']['position']:
					alt = packet['decoded']['position']['altitude']
				cotId = users[meshId]['cotId']
				print(f"Sending PLI CoT Lat: {lat} Lon: {lon} Alt: {alt}")
				takserver.send(mkcot.mkcot(cot_identity="friend"
					, cot_stale = 10
					, cot_dimension="land-unit",cot_typesuffix="E-C-T"
					, cot_lat=lat, cot_lon=-lon, cot_hae=alt
					, cot_id=cotId, team_name="Red"
					, cot_callsign=meshLongName))
				time.sleep(1)
				print("read the response")
				print(takserver.read())
		print()
	if packetType == 'data':
		meshId = packet['from']
		if meshId in users:
			meshLongName = users[meshId]['meshLongName']
			cotId = users[meshId]['cotId']
			print(f"Received Data Packet from {meshLongName}")
			if 'typ' in packet['decoded']['data']:
				dataType = packet['decoded']['data']['typ']
				if dataType == 'CLEAR_TEXT':
					target_msg = packet['decoded']['data']['text']
					# Messages have a unique uid- critical
					event_uid = "GeoChat." + cotId + "." + "All Chat Rooms" + "." + str(uuid.uuid4())
					print(f"Message: {target_msg}")
					cot_xml = mkcot.mkcot(tgt_call="All Chat Rooms"
						, tgt_uid="All Chat Rooms"
						, tgt_msg=target_msg
						# can be set as needed
						, cot_type="b-t-f" , cot_how="h-g-i-g-o", cot_typesuffix=""
						# takpak defaults are OK
						, cot_identity = "" ,  cot_dimension = ""
						, cot_id=event_uid
						# this differentiates the CoT as a message
						, sender_uid=cotId
						, cot_callsign=meshLongName
					)
					takserver.flush()  # flush the xmls the server sends
					takserver.send(cot_xml)
					print()
		else:
			meshLongName = packet['from']
			print(f"Received Data Packet from {meshLongName}")

#logging.basicConfig(level=logging.INFO) # level=10

#-----------------------------------------------------------------------------------------

my_uid = str(socket.getfqdn())
my_call = my_uid
# Now add a UUID, without the time component
my_uid = my_uid + "-" + str(uuid.uuid1())[-12:]
my_call = my_call + "-" + my_uid[-4:]

# substantiate the class
takserver = takcot()

# Now open server
print("Opening TAK Server")
testsock = takserver.open(TAK_IP)

#print("open return is:")
#print(testsock)


#connect_xml=cot_xml
print()
print("send a connect")
takserver.flush()  # flush the xmls the server sends
#print(takserver.read())  # read all the server CoT's, will send last + the connct

# send the connect string, server does not echo
takserver.send(mkcot.mkcot(cot_type="t", cot_how="h-g-i-g-o"))
#print("read the Connect response")
#print(takserver.read())  # read all the server CoT's, will send last + the connct
print("Flush the server response")
takserver.flush()  # flush the xmls the server sends
time.sleep(1)
pingThread = Thread(target=pingTimer)
pingThread.start()

users = {}
interface = meshtastic.StreamInterface()
#pub.subscribe(onNodeUpdate, "meshtastic.node.updated")
pub.subscribe(onReceive, "meshtastic.receive")

# Always need to close out the connection
# good practice to include reading anything the server pushed
# to prevent broken pipe errors on the server

#takserver.flush()  # flush the xmls the server sends
#print("Closing TAK Server")
#takserver.takclose()
