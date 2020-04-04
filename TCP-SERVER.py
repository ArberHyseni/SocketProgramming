import socket, threading, re
from random import seed, randint
from datetime import datetime

#regular expression function, to eliminate double tripple, ... n spaces, using re module and lstrip() functions, this is also one of the most used code in this project
def rexp(str):
    str = re.sub(' +', ' ', str)
    str = str.lstrip()
    return str.split(' ')

def cmToFeet(value):
    if(value.isdigit()):
        ft = float(value)*0.032802
        print("%.2f" %ft)
    else:
        raise Exception("No strings allowed for this function")

def feetToCm(value):
    if(value.isdigit()):
        cm = float(value/0.032802)
        print("%.2f" %cm)
    else:
        raise Exception("No strings allowed for this function")

def kmToMiles(value):
    if(value.isdigit()):
        miles = value * 0.621371
        print("%.2f" %miles)
    else:
        raise Exception("No strings allowed for this function")
  
def milesToKm(value):
    if(value.isdigit()):
        km = value/0.621371
        print("%.2f" %km)
    else:
        raise Exception("No strings allowed for this function")    

def IPADDRESS():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"IP Address: {ip_address}")

#Funksioni per numerimin e zanoreve dhe bashketingelloreve(numrave dhe karaktereve tjera po ashtu)

#Reverse string with slicing
def reverse_string(s):
    if(s.isalpha()):
        revres = s[::-1]
    elif not (s.isalpha()):
        raise Exception("Only words from the alphabet are allowed")
    
    return revres

#Simple boolean if statement
def isPalindrome(s):
    rev = s[::-1]
    if(s.isalpha()):
        if (s == rev):
            return True
    elif not (s.isalpha()):
        raise Exception("Only words from the alphabet are allowed")
    else:
        return False

#Generate random numbers with seed and randint from two libraries
lst = []
def generateRandomNumber(): 
    forseed = randint(1, 100)
    seed(forseed)
    for _ in range(5):
	    rvalue = randint(1, 35) 
	    lst.append(rvalue)
    return lst

def checkTime(): #ketu hyhet ne perdorim librari e gatshme datetime
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
    print (gcf)
    return gcf

#uInput = input("Enter input:")
#vInput = rexp(uInput)
#if(vInput[0] == 'gcf'):
 #   GCF(int(vInput[1]), int(vInput[2]))


class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print('Klienti u lidh me %s ne portin %s' %clientAddress)
    def run(self):
        mesazhi = ''
        while True:
            data = self.csocket.recv(2048)
            mesazhi = data.decode()
            mesazhi = rexp(mesazhi)
            if(mesazhi[0] == 'ipaddress'):
                IPADDRESS()
            elif(mesazhi[0] == 'count'):
                komanda = countLetters(mesazhi[1])
                self.csocket.send(bytes(komanda,'UTF-8'))
                
            elif(mesazhi[0] == 'reverse'):
                reverse_string(mesazhi[1])
            elif(mesazhi[0] == 'palindrome'):
                print(isPalindrome(mesazhi[1]))
            elif(mesazhi[0] == 'time'):
                checkTime()
            elif(mesazhi[0] =='game'):
                generateRandomNumber()
            elif(mesazhi[0] == 'gcf'):
                findGCF(int(mesazhi[1]), int(mesazhi[2]))
            elif(mesazhi[0] == 'convert' and mesazhi[1] == 'cmtofeet'):
                cmToFeet(float(mesazhi[3]))
            elif(mesazhi[0] == 'convert' and mesazhi[1] == 'feettocm'):
                feetToCm(float(mesazhi[3]))
            elif(mesazhi[0] == 'convert' and mesazhi[1] == 'kmtomiles'):
                kmToMiles(float(mesazhi[3]))
            elif(mesazhi[0] == 'convert' and mesazhi[1] == 'milestokm'):
                milesToKm(float(mesazhi[3]))
            elif(mesazhi[1]=='bye'): #dalja nga while nese bye jepet nga klienti
                break
            else:
                raise Exception("Wrong Syntax")
            
            #print (mesazhi)
            self.csocket.send(bytes(mesazhi,'UTF-8'))
        print ("Client at", clientAddress,"disconnected...")
LOCALHOST = "127.0.0.1"
PORT = 1200
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Serveri u startua")
print("Ne pritje per ndonje konektim.")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()

