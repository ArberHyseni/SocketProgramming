import socket, re

def upperC(value):
    fjaliaup = value.upper()
    return fjaliaup

def countLetters(strp):
    strp = strp.lower()
    i = 0
    vowel = 0
    consonant = 0
    while i < len(strp):
        if re.match(r"[a-z]", strp[i]):
            if re.match(r"[aeiouy]", strp[i]):
                vowel = vowel + 1
            else:
                consonant = consonant + 1
        i = i+1
    result = f'C {consonant} V {vowel}'
    return result



serverName = ''
serverPort = 1200

serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverS.bind((serverName,serverPort))
print('Serveri eshte startuar ne localhost ne portin: ' + str(serverPort))
serverS.listen(5)
print('Serveri eshte duke pritur per ndonje kerkese')

while True:
    clientS, address = serverS.accept()
    print('---------------------------------------')
    print('Klienti u lidh me %s ne portin %s' %address)
    clientInput = clientS.recv(2048)
    print('Kerkesa nga klienti:' + str(clientInput.decode("utf-8")))
    clientInput = countLetters(clientInput)
    print('Kalkulimi nga serveri: ' + str(clientInput.decode("utf-8")))
    clientS.sendall(clientInput)
    clientS.close()
    print('Perfundoj komunikimi')

