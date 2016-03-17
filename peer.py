import socket, ast

# Server Details
UDP_IP = "localhost"
UDP_PORT = 3610

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def SendToServer(message):
	sock.sendto(message, (UDP_IP, UDP_PORT))

def GetPeerAddress(PeerName):
	SendToServer("RequestPeerAddress$#$"+PeerName)
	recv_data, addr = sock.recvfrom(2048)
	return recv_data

def GetAddressFromString(address):
	return (address.split(',')[0][1:][1:-1],int(address.split(',')[1][:-1]))

def SendToPeer(Peer,message):
	address = GetPeerAddress(Peer)
	print "Send to peer", Peer, message
	sock.sendto(message, GetAddressFromString(address))

ServerAddress = None
Peers = None

name = raw_input("Enter Name:")
SendToServer("connect$#$"+name)


while True:
	try:
		recv_data, addr = sock.recvfrom(2048)
		if not ServerAddress:
			ServerAddress = addr
		peer = raw_input("Peer Name: ")
		message = raw_input("Enter Message: ")
		SendToPeer(peer,message)
		recv_data, addr = sock.recvfrom(2048)
		print recv_data, addr
	except socket.error as (code, msg):
		if code != errno.EINTR:
			print "Test"