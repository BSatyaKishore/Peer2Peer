## Peer to Peer
A simple implementation of Peer to Peer Messaging Application with Central Server in Python using UDP

## Synopsis
There are 2 parts in the project:
1. Server:
   The main work of the server is to get the address of all the Peers and send it to other Peers on request
2. Client:
   The Client first sends a connect message to the server. The Client to Send a message to peer, first resolves the address of the peer by asking it to server. Then Sends the message to the address and waits for a reply (or any message).

## Running
1. Change the UDP_IP and UDP_PORT in server.py to correct parameters. And run server.py
2. Update the peer.py code with the corresponding parameters.
3. Run peer.py and give it a peer name. And then run another instance of peer.py from another PC or same PC and give it a name and Send a message to the first (this message will be void).
4. From next, you can chat (send message and wait for reply)
5. Requirements: The server.py should have an IP which can be pingable from client PCs

## Contributors
[MySelf](http://www.cse.iitd.ac.in/~cs5120284)

## License
Open Source. MIT Licence
