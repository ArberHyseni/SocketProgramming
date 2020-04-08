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
        vinput = rexp(indata)
        #While true
        if vinput[0] == 'ipaddress':
            print("Received from client: ", indata)
            exe = self.data
            exe = str(exe[0]).encode()
            self.server.sendto(exe,self.data)
        elif vinput[0] == 'port':
            print("Received from client: ", indata)
            exe = self.data
            exe = str(exe[1]).encode()
            self.server.sendto(exe,self.data)                    
        elif(vinput[0] == 'count'):
            exe = COUNT(vinput[1])
            exe = exe.encode()
            self.server.sendto(exe,self.data)
            print ("Received from client: ", indata)
        elif(vinput[0] == 'reverse'):
            print ("Received from client: ", indata)
            exe = REVERSE(vinput[1])
            exe = exe.encode()
            self.server.sendto(exe,self.data)
        elif(vinput[0] == 'palindrome'):
            print ("Received from client: ", indata)
            exe = Palindrome(vinput[1])
            exe = exe.encode()
            self.server.sendto(exe,self.data)
        elif(vinput[0] == 'time'):
            print ("Received from client: ", indata)
            exe = Time()
            exe = exe.encode()
            self.server.sendto(exe,self.data)
        elif(vinput[0] == 'game'):
            print ("Received from client: ", indata)
            exe = GAME()
            listToStr = ' '.join(map(str, exe)) #list to string
            listToStr = listToStr.encode()
            self.server.sendto(listToStr,self.data)
        elif(vinput[0] == 'gcf'):
            print ("Received from client: ", indata)
            exe = GCF(int(vinput[1]), int(vinput[2]))
            exes = str(exe)
            exes = exes.encode()
            self.server.sendto(exes,self.data)
        elif(vinput[0] == 'convert' and vinput[1] == 'cmtofeet'):
            print ("Received from client: ", indata)
            exe = cmToFeet(float(vinput[2]))
            exe = exe.encode()
            self.server.sendto(exe,self.data)
        elif(vinput[0] == 'convert' and vinput[1] == 'feettocm'):
            print ("Received from client: ", indata)
            exe = feetToCm(float(vinput[2]))
            exe = exe.encode()
            self.server.sendto(exe,self.data)
        elif(vinput[0] == 'convert' and vinput[1] == 'kmtomiles'):
            print ("Received from client: ", indata)
            exe = kmToMiles(float(vinput[2]))
            exe = exe.encode()
            self.server.sendto(exe,self.data)
        elif(vinput[0] == 'convert' and vinput[1] == 'milestokm'):
            print ("Received from client: ", indata)
            exe = milesToKm(float(vinput[2]))
            exe = exe.encode()
            self.server.sendto(exe,self.data)
        elif indata == 'bye': #KQYR EDHE NIHER
            print("Bye")
        else:
            self.server.sendto(sdata,self.data)
            print ("Client at " + str(self.data) + " has disconnected...")  #Shto te secila
                               
if __name__ == '__main__': 
		server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		server.bind(('localhost',8093))
		print ("UDP socket server is established")
		while True:
            #Recieve information from the client
			data, addr = server.recvfrom(1024)
            #Allocate a new thread to the client
			Clientthread = Server(addr,data,server)
            #Start the thread for the new client
			Clientthread.start()
    