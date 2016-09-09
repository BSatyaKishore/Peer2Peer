import socket,sys

UDP_IP = "localhost"	#localhost"#"10.208.20.9"#"10.208.20.211"#"localhost"
UDP_PORT = 3610
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

connections = {}

def SendToPeer(data, addr):
	print connections, data
	if data == "SERVER":
		sock.sendto(str(UDP_IP,UDP_PORT), addr)
		return
	print "Sending ", str(connections[data]), addr
	sock.sendto(str(connections[data]), addr)
	#print "Sent"

while True:
	rec_data, addr = sock.recvfrom(2048) # buffer size is 1024 bytes
	data = rec_data.split("$#$")
	print "Recieved ", rec_data, addr, data, data[0] == "RequestPeerAddress"
	if data[1] in connections.keys():
		if data[0] == "disconnect":
			del connections[str(data[1])]
		elif data[0] == "RequestPeerAddress":
			SendToPeer(data[1],addr)
	else:
		if data[0] == "connect":		
			connections[str(data[1])] = addr
			SendToPeer(str(data[1]),addr)

		

