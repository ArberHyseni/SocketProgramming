import socket, threading, re
from random import seed, randint
from datetime import datetime
from ipaddress import IPv4Address, IPv4Network
#client input validation
def regex(string):
    string = string.lower()
    string = re.sub(' +', ' ', string)
    string = string.lstrip() #Left strip to remove whitespaces
    return string.split(' ') #Split for splitting input in spaces

def COUNT(value):
    if(value.isalpha()): #A eshte shkronje alfabetike
        vow = 0
        con = 0
        list1 = ["a", "e", "i", "o", "u"] #krijimi i nje liste
        for char in value: 
            if char in list1: #nese char gjendet ne liste
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
        #Show exception on terminal for invalid input
        raise Exception("Only words from the alphabet are allowed") 
    
    return revres

def Palindrome(s):
    true = "True"
    false = "False"
    rev = s[::-1] #slicing method to reverse given string
    if(s.isalpha()):
        if (s == rev):
            return true
        else:
            return false
    else:
        result = "Only numbers allowed"
        return result

def GAME():
    lst = []
    forseed = randint(1, 100) #random number generator
    seed(forseed)
    for _ in range(5):
	    rvalue = randint(1, 35) #generate random numbers between 1 and 35
	    lst.append(rvalue) #append to list
    return lst

def Time(): #ketu hyhet ne perdorim librari e gatshme datetime
    time = datetime.now()  
    date_string = time.strftime("%d/%m/%Y %H:%M:%S") #string format for time
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

def passwordStrength(s):
    # Enter password text
    length = re.compile(r'(\w{8,})')  # Check if password has atleast 8 characters
    lower = re.compile(r'[a-z]+') # Check if at least one lowercase letter
    upper = re.compile(r'[A-Z]+')# Check if atleast one upper case letter
    digit = re.compile(r'[0-9]+') # Check if at least one digit.
    special = re.compile(r'[!@#$%^&*_.]+')
    if length.findall(s) == []:  # Checks if the password does not contain 8 characters, findall() kthen string array
        result = 'Your Password must contain at least 8 characters'
    elif lower.findall(s)==[]: # Checks if the password does not contain a lowercase character
        result = 'Your Password must contain at least one lowercase character'
    elif upper.findall(s)==[]: # Checks if the password does not contain an uppercase character
        result = 'Your Password must contain at least one uppercase character'
    elif digit.findall(s)==[]: # Checks if the password does not contain a digit character
        result = 'Your Password must contain at least one digit character'
    elif special.findall(s)==[]: # Checks if the password does not contain a special char
        result = 'Your Password must contain at least one special character'
    else:  # if the above 4 conditions are successfully passed, pringt out a message saying the password is strong.
        result = 'Your password is strong, congratulations!'
        
    return result

def ipclass(s):
    try:
        ip = IPv4Address(s) #represent and manipulate single ipv4 addresses
        # ipv4network represents and manipulates 32-bit IPv4 network and addresses.
        classA = IPv4Network(("1.0.0.1", "255.0.0.0")) # or IPv4Network("10.0.0.0/8")
        classB = IPv4Network(("128.1.0.1", "255.255.0.0")) # or IPv4Network("128.1.0.1/16")
        classC = IPv4Network(("192.0.1.1", "255.255.255.0")) # or IPv4Network("192.0.1.1/24")
        if ip in classA:
            return "Given ip is in Class A"
        elif ip in classB:
            return "Given ip is in Class B"
        elif ip in classC:
            return "Given ip is in Class C"
    except:
        return "error"

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self): #qekjo run(self) edhe init ma nalt spo e kom bash te qarte qa bojn, e po ma hupin zumin qito hahahaha
        self.csocket.send(bytes("Hi...",'utf-8'))
        msg = ''
        flist = ["count", "convert", "game", "palindrome", "gcf", "reverse", "time", "hi", "Hi", "ipclass", "passwordstrength"]
        while True:
            data = self.csocket.recv(2048) #ose 1024
            msg = data.decode()
            vinput = regex(msg)
            if vinput[0] == 'ipaddress':
                exe = str(clientAddress[0])
                self.csocket.send(bytes(exe,'UTF-8'))
                print ("Received from client: ", msg)
            elif vinput[0] == 'port':
                exe = str(clientAddress[1])
                self.csocket.send(bytes(exe,'UTF-8'))
                print ("Received from client: ", msg)
            elif(vinput[0] == 'count'):
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
            elif(vinput[0] == 'gcf'): #---------------------------------------------- SHTO
                print ("Received from client: ", msg)
                exe = GCF(int(vinput[1]), int(vinput[2]))
                exes = str(exe) #int to str
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
            elif(vinput[0] == 'passwordstrength'): # E RE TESTOJE
                asteriks = '*' * len(vinput[1])
                print ("Received from client: " + vinput[0] + ' ' + asteriks)
                exe = passwordStrength(vinput[1])
                self.csocket.send(bytes(exe,'UTF-8'))
            elif(vinput[0] == 'ipclass'): # e re
                print ("Received from client: ", msg)
                exe = ipclass(vinput[1])
                self.csocket.send(bytes(exe,'UTF-8'))
            elif vinput[0] not in flist:
                print(vinput[0])
                exe = "<error>"
                self.csocket.send(bytes(exe,'UTF-8'))
            elif vinput[0]=='bye':
                print ("From client", msg)
                self.csocket.send(bytes(msg,'UTF-8'))
                break
            #elif qitu me bo diqka if input = 'changeport' ose 'reconnect'
                #insert some code here
        print ("Client at ", clientAddress , " disconnected...")
LOCALHOST = "localhost"
PORT = 13000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start() # edhe qikjo pjese ne fund eshte, se body eshte krejt funksione qe i kom thirr