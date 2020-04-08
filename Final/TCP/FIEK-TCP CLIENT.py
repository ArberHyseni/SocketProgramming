import socket
SERVER = "localhost"
PORT = 13000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT)) # me kete krijohet lidhja me tcp server
client.sendall(bytes("Hi",'UTF-8'))
while True:
  in_data =  client.recv(1024)
  print("From Server :" ,in_data.decode())
  out_data = input("Operacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, PASSWORDSTRENGTH, IPCLASS)")
  client.sendall(bytes(out_data,'UTF-8'))
  if out_data=='bye':
    break
print("Connection with server is done")
client.close()
