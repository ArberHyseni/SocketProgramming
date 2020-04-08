import socket, threading, re
from random import seed, randint
from datetime import datetime

def rexp(string): #Validimi i inputit
    string = string.lower()
    string = re.sub(' +', ' ', string)
    string = string.lstrip() #Left strip to remove whitespaces
    return string.split(' ') #Split per perpunim te te dhenave ne input

def COUNT(value):
    if(value.isalpha()): #A eshte shkronje alfabetike
        vow = 0
        con = 0
        list1 = ["a", "e", "i", "o", "u"]
        for char in value:
            if char in list1:
                vow+=1
            elif char not in list1 and char>="a" and char<="z":
                con+=1
    else:
        raise Exception("Lejohen vetem shkronja te alfabetit.")
    
    result = f'Consonant {con} Vowel {vow}' #return permes f string
    return result

def cmToFeet(value):
    ft = float(value)*0.032802
    result = "Feet= %.2f" % ft
    return result

def feetToCm(value):
    cm = float(value/0.032802)
    result = "Cm= %.2f" % cm
    return result

def kmToMiles(value):
    
    miles = value * 0.621371
    result = "Miles= %.2f" % miles
    return result

def milesToKm(value):
    
    km = value/0.621371
    result = "Km= %.2f" % km
    return result

def REVERSE(s):
    if(s.isalpha()):
        revres = s[::-1]
    elif not (s.isalpha()):
        raise Exception("Only words from the alphabet are allowed")
    
    return revres

def Palindrome(s):
    true = "True"
    false = "False"
    rev = s[::-1]
    if(s.isalpha()):
        if (s == rev):
            return true
    elif not (s.isalpha()):
        raise Exception("Only words from the alphabet are allowed")
    else:
        return false

lst = []
#kqyre edhe niher
def GAME(): 
    forseed = randint(1, 100)
    seed(forseed)
    for _ in range(5):
	    rvalue = randint(1, 35) 
	    lst.append(rvalue)
    return lst

def Time(): #ketu hyhet ne perdorim librari e gatshme datetime
    time = datetime.now()  
    date_string = time.strftime("%d/%m/%Y %H:%M:%S")
    return date_string

#Find greatest common factor
def GCF(x, y):
    if x > y:
        little = y
    else:
        little = x
    for i in range(1, little+1): #for loop prej 1 deri te me i vogli +1
        if ((x % i == 0) and (y % i == 0)): #operacioni modulo
            gcf = i
    
    return gcf

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        self.csocket.send(bytes("Hi...",'utf-8'))
        msg = ''
        flist = ["count", "convert", "game", "palindrome", "gcf", "reverse", "time", "hi", "Hi"]
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            vinput = rexp(msg)
            if(vinput[0] == 'count'):
                exe = COUNT(vinput[1])
                self.csocket.send(bytes(exe,'UTF-8'))
                print ("Received from client: ", msg)
            elif(vinput[0] == 'reverse'):
                print ("Received from client: ", msg)
                exe = REVERSE(vinput[1])
                self.csocket.send(bytes(exe,'UTF-8'))
            elif(vinput[0] == 'palindrome'):
                print ("Received from client: ", msg)
                exe = Palindrome(vinput[1])
                self.csocket.send(bytes(exe,'UTF-8'))
            elif(vinput[0] == 'time'):
                print ("Received from client: ", msg)
                exe = Time()
                self.csocket.send(bytes(exe,'UTF-8'))
            elif(vinput[0] == 'game'):
                print ("Received from client: ", msg)
                exe = GAME()
                listToStr = ' '.join(map(str, exe)) #list to string
                self.csocket.send(bytes(listToStr,'UTF-8'))
            elif(vinput[0] == 'gcf'):
                print ("Received from client: ", msg)
                exe = GCF(int(vinput[1]), int(vinput[2]))
                exes = str(exe)
                self.csocket.send(bytes(exes,'UTF-8'))
            elif(vinput[0] == 'convert' and vinput[1] == 'cmtofeet'):
                print ("Received from client: ", msg)
                exe = cmToFeet(float(vinput[2]))
                self.csocket.send(bytes(exe,'UTF-8'))
            elif(vinput[0] == 'convert' and vinput[1] == 'feettocm'):
                print ("Received from client: ", msg)
                exe = feetToCm(float(vinput[2]))
                self.csocket.send(bytes(exe,'UTF-8'))
            elif(vinput[0] == 'convert' and vinput[1] == 'kmtomiles'):
                print ("Received from client: ", msg)
                exe = kmToMiles(float(vinput[2]))
                self.csocket.send(bytes(exe,'UTF-8'))
            elif(vinput[0] == 'convert' and vinput[1] == 'milestokm'):
                print ("Received from client: ", msg)
                exe = milesToKm(float(vinput[2]))
                self.csocket.send(bytes(exe,'UTF-8'))
            elif vinput[0] not in flist:
                print(vinput[0])
                ignore = "."
                self.csocket.send(bytes(ignore,'UTF-8')) # para ksaj veq kjo ska bo, watch out
                continue
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