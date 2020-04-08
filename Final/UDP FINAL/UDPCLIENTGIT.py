import socket
#Set the port
serverAddressPort   = ("localhost", 8093)
#Create a UDP socket connection
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Allow the user to input a message for the server
message = input("Message to server:")

mbytes = str.encode(message)
#Send the message to the server
clientSocket.sendto(mbytes, serverAddressPort)

#Receive the reply from the server
ReceivedFromServer, serverAddress = clientSocket.recvfrom(1024) #1024bytes
srvinput = ReceivedFromServer.decode() 
print("Pergjigjja:" + srvinput)
#Allow new message to be sent to the server
print("Connection closed")
#Close the client socket
clientSocket.close()
