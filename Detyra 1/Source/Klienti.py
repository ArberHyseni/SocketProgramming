import socket

serverName = 'localhost'
serverPort = 1200
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverName,serverPort))

var = input("Jeni lidhur me serverin, shkruani kerkesen: ")
s.sendall(str.encode(var))

mesazhi = ''
while True:
    data = s.recv(1024)
    if len(data) <= 0:
        break
    mesazhi += data.decode("utf-8")
print('Te dhenat e pranuara nga serveri: ', mesazhi)
s.close()



