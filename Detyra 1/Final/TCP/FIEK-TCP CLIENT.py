import socket
SERVER = "localhost"
PORT = 13000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket object
client.connect((SERVER, PORT))# Connect to a remote socket at given address
client.sendall(bytes("Hi",'UTF-8')) # send Hi message to socket
while True:
    serverdata = client.recv(1024) #receive welcome message
    print("From Server:" ,serverdata.decode())
    clientdata = input("Operacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, PASSWORDSTRENGTH, FIBONACCI): ")
    client.sendall(bytes(clientdata,'UTF-8'))
    serverdata = client.recv(2048) # get the server data
    print("Pergjigjja: " ,serverdata.decode())
    while True:
        answer = input('Run again? (p/j): ')
        if answer == 'p':
            clientdata = input("Operacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, PASSWORDSTRENGTH, FIBONACCI): ")
            client.sendall(bytes(clientdata,'UTF-8'))
            serverdata = client.recv(1024)
            print("Pergjigjja: " ,serverdata.decode())
            continue
        elif answer == 'j':
            print ('Goodbye')
            client.sendall(bytes("bye",'UTF-8'))
            break
        
    break
client.close() # close connection
print("Connection with server is done")
