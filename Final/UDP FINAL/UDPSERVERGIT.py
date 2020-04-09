import threading, socket, re
from random import seed, randint
from datetime import datetime

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
        return "Lejohen vetem shkronja te alfabetit."

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
        return "Only words from the alphabet are allowed"
    
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
    digit = re.compile(r'[0-9]+') # Check if at least one digit.
    special = re.compile(r'[!@#$%^&*_.]+')
    if length.findall(s) == []:  # Checks if the password does not contain 8 characters, findall() kthen string array
        result = 'Your Password must contain at least 8 characters'
    elif lower.findall(s)==[]: # Checks if the password does not contain a lowercase character
        result = 'Your Password must contain at least one lowercase character'
    elif digit.findall(s)==[]: # Checks if the password does not contain a digit character
        result = 'Your Password must contain at least one digit character'
    elif special.findall(s)==[]: # Checks if the password does not contain a special char
        result = 'Your Password must contain at least one special character'
    else:  # if the above 4 conditions are successfully passed, pringt out a message saying the password is strong.
        result = 'Your password is strong, congratulations!'
        
    return result

def Fibonacci(n):
   if n<0:
      print("No such number allowed!")
   # First Fibonacci number is 0 (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...)
   elif n==1:
      return 0
   # Second Fibonacci number
   elif n==2:
      return 1
   else:
      return Fibonacci(n-1)+Fibonacci(n-2)

#Klasa Server qe merr thread ne parameter
class Server(threading.Thread):
    def __init__(self,addr,data,server): # konstruktori i klases
        threading.Thread.__init__(self)
        self.data = addr
        self.message = data
        self.server = server
    def run(self):
        indata = (self.message).decode()
        sdata = indata.encode()
        vinput = regex(indata)
        if vinput[0] == 'ipaddress':
            print("Received from client: ", indata)
            exe = self.data
            exe = str(exe[0]).encode()
            self.server.sendto(exe,self.data)
            print ("Client at " + str(self.data) + " has disconnected...") 
        elif vinput[0] == 'port':
            print("Received from client: ", indata)
            exe = self.data
            exe = str(exe[1]).encode()
            self.server.sendto(exe,self.data)  
            print ("Client at " + str(self.data) + " has disconnected...")                   
        elif(vinput[0] == 'count'):
            exe = COUNT(vinput[1])
            exe = exe.encode()
            self.server.sendto(exe,self.data)
            print ("Received from client: ", indata)
            print ("Client at " + str(self.data) + " has disconnected...") 
        elif(vinput[0] == 'reverse'):
            print ("Received from client: ", indata)
            exe = REVERSE(vinput[1])
            exe = exe.encode()
            self.server.sendto(exe,self.data)
            print ("Client at " + str(self.data) + " has disconnected...") 
        elif(vinput[0] == 'palindrome'):
            print ("Received from client: ", indata)
            exe = Palindrome(vinput[1])
            exe = exe.encode()
            self.server.sendto(exe,self.data)
            print ("Client at " + str(self.data) + " has disconnected...") 
        elif(vinput[0] == 'time'):
            print ("Received from client: ", indata)
            exe = Time()
            exe = exe.encode()
            self.server.sendto(exe,self.data)
            print ("Client at " + str(self.data) + " has disconnected...") 
        elif(vinput[0] == 'game'):
            print ("Received from client: ", indata)
            exe = GAME()
            listToStr = ' '.join(map(str, exe)) #list to string
            listToStr = listToStr.encode()
            self.server.sendto(listToStr,self.data)
            print ("Client at " + str(self.data) + " has disconnected...") 
        elif(vinput[0] == 'gcf'):
            if(vinput[1].isdigit() and vinput[2].isdigit()):
                print ("Received from client: ", indata)
                exe = GCF(int(vinput[1]), int(vinput[2]))
                exes = str(exe) #int to str
                exes = exes.encode()
                self.server.sendto(exes,self.data)
                print ("Client at " + str(self.data) + " has disconnected...")
            else:
                print ("Received from client: ", indata)
                errors = "Error"
                errors = errors.encode()
                self.server.sendto(errors,self.data)
                print ("Client at " + str(self.data) + " has disconnected...") 
        elif(vinput[0] == 'convert' and vinput[1] == 'cmtofeet'):
            if vinput[2].isdigit():
                print ("Received from client: ", indata)
                exe = cmToFeet(float(vinput[2]))
                exe = exe.encode()
                self.server.sendto(exe,self.data)
                print ("Client at " + str(self.data) + " has disconnected...")
            else:
                print ("Received from client: ", indata)
                errors = "Error"
                errors = errors.encode()
                self.server.sendto(errors,self.data)
                print ("Client at " + str(self.data) + " has disconnected...")
        elif(vinput[0] == 'convert' and vinput[1] == 'feettocm'):
            if vinput[2].isdigit():
                print ("Received from client: ", indata)
                exe = feetToCm(float(vinput[2]))
                exe = exe.encode()
                self.server.sendto(exe,self.data)
                print ("Client at " + str(self.data) + " has disconnected...")
            else:
                print ("Received from client: ", indata)
                errors = "Error"
                errors = errors.encode()
                self.server.sendto(errors,self.data)
                print ("Client at " + str(self.data) + " has disconnected...")
        elif(vinput[0] == 'convert' and vinput[1] == 'kmtomiles'):
            if vinput[2].isdigit():
                print ("Received from client: ", indata)
                exe = kmToMiles(float(vinput[2]))
                exe = exe.encode()
                self.server.sendto(exe,self.data)
                print ("Client at " + str(self.data) + " has disconnected...")
            else:
                print ("Received from client: ", indata)
                errors = "Error"
                errors = errors.encode()
                self.server.sendto(errors,self.data)
                print ("Client at " + str(self.data) + " has disconnected...")
        elif(vinput[0] == 'convert' and vinput[1] == 'milestokm'):
            if vinput[2].isdigit():
                print ("Received from client: ", indata)
                exe = cmToFeet(float(vinput[2]))
                exe = exe.encode()
                self.server.sendto(exe,self.data)
                print ("Client at " + str(self.data) + " has disconnected...")
            else:
                print ("Received from client: ", indata)
                errors = "Error"
                errors = errors.encode()
                self.server.sendto(errors,self.data)
                print ("Client at " + str(self.data) + " has disconnected...")
        else:
            self.server.sendto(sdata,self.data)
            print ("Client at " + str(self.data) + " has disconnected...") 
                               
if __name__ == '__main__': # set variable __name__, and then executes all of the code found in the file.
		server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # SOCK_DGRAM, create datagram socket for UDP protocol
		server.bind(('localhost',13000))
		print ("UDP socket server is established")
		while True:
            #Recieve information from the client
			data, addr = server.recvfrom(1024)
            #Allocate a new thread to the client
			Clientthread = Server(addr,data,server)
            #Start the thread for the new client
			Clientthread.start()
    