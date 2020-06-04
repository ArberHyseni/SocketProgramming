import socket

#Set the port
#Set the port
serverAddressPort   = ("localhost", 8093)
# serverAddressPort   = ("localhost", 20001)
# addressstr =  ' '.join(serverAddressPort)
#Create a UDP socket connection
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Allow the user to input a message for the server
message = input("Message to server:")

#While the client has not ellected to quit
mbytes = str.encode(message)
#Send the message to the server
clientSocket.sendto(mbytes, serverAddressPort)

#Receive reply from the server
ReceivedFromServer, serverAddress = clientSocket.recvfrom(1024)
srvinput = ReceivedFromServer.decode()
print("Server Reply: " + srvinput)
#Allow new message to be sent to the server
print("Connection closed")
#Send the quit message to the server
#Close the client socket
clientSocket.close()
# Send the quit message to the server
# clientSocket.sendto(mbytes, serverAddressPort)

# #Close the client socket
# clientSocket.close()