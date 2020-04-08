import threading, socket, re
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


#Krijimi i klases server
class Server(threading.Thread):        
    def __init__(self,addr,data,server):
        threading.Thread.__init__(self)
        self.data = addr
        self.message = data
        self.server = server
    def run(self):
        indata = (self.message).decode()
        sdata = indata.encode()
        print ("The client has sent: " + indata)
        #If bye close connection with server, also shutdown server
        if indata == 'bye':
            print ("Client at " + str(self.data) + " has disconnected...")
        elif indata == 'ipaddress':
            address = self.data
            ipaddress = address[0]
            self.server.sendto(str(ipaddress),self.data)
            print ("Client at " + str(self.data) + " has disconnected...")
        else:
            print ("Client at " + str(self.data) + " has disconnected...")
            self.server.sendto(str(ipaddress),self.data)
            
                                   
if __name__ == '__main__':
	
        #Set up the socket to use UDP 
		server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #Bind to the client on the port
		server.bind(('localhost',8093))
		print ("UDP socket server is established")
		while True:
            #Recieve information from the client
			data, addr = server.recvfrom(1024)
            #Allocate a new thread to the client
			Clientthread = Server(addr,data,server)
            #Start the thread for the new client
			Clientthread.start()
    