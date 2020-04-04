import socket, threading, re
from datetime import datetime

def rexp(string): #Validimi i inputit
    string = string.lower()
    string = re.sub(' +', ' ', string)
    string = string.lstrip() #Left strip to remove whitespaces
    return string.split(' ') #Split per perpunim te te dhenave ne input

def REVERSE(s):
    if(s.isalpha()):
        revres = s[::-1]
    elif not (s.isalpha()):
        raise Exception("Only words from the alphabet are allowed")
    
    return revres

def Time(): #ketu hyhet ne perdorim librari e gatshme datetime
    time = datetime.now()  
    date_string = time.strftime("%d/%m/%Y %H:%M:%S")
    return date_string

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            vinput = rexp(msg)
            if vinput[0] == 'time':
                print ("From client", msg)
                exe = Time()
                self.csocket.send(bytes(exe,'UTF-8'))
            elif vinput[0] == 'reverse':
                print ("From client", msg)
                exe = REVERSE(vinput[1])
                self.csocket.send(bytes(exe,'UTF-8'))
            elif vinput[0]=='bye':
                print ("From client", msg)
                self.csocket.send(bytes(msg,'UTF-8'))
                break
        print ("Client at ", clientAddress , " disconnected...")
LOCALHOST = "127.0.0.1"
PORT = 8092
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()