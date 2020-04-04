import socket
SERVER = "127.0.0.1"
PORT = 1200
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
userInput = input("Operacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT)? ")
client.sendall(bytes("This is from Client",'UTF-8'))

while True:
  input_data = client.recv(1024)
  print("From Server :",input_data.decode())
  out_data = input()
  client.sendall(bytes(out_data,'UTF-8'))
  if out_data=='bye':
    break

client.close()