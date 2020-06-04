#Web Server 
import socket
import codecs

serverName = ''
serverPort = 9999

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#reuse adresat e klientave qe kane deshtuar ne lidhje...
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(10)
print(f'Serveri eshte duke punuar ne portin {serverPort}')

while True:
    clientSocket, address = serverSocket.accept()
    pranimi = clientSocket.recv(1024)
     
    #duhet te shqyrtohet kerkesa(pranimi)
    #GET /fiek/ushtrimet/index.html HTTP/1.1
    kerkesa = pranimi.decode("utf-8")
    #check if GET
    get = kerkesa[0:3]
    if get != 'GET': 
        break
    #e gjejme pozicionin e fjales HTTP/1.
    index = int(kerkesa.index('HTTP/1.'))
    #/fiek/ushtrimet/index.html
    pathi = kerkesa[4:index]
    folderCheck = pathi.count('/')
    folder = ''
    file = ''
    if folderCheck > 1:
        #kemi follder
        #/fiek/ushtrimet/
        folder = pathi[pathi.find('/'):pathi.rfind('/')+1]
        #/index.html
        file = pathi[pathi.rfind('/')+1:]
    else: 
        #skemi follder por vetem fjall
        #/index.html
        file = pathi[1:]
    
    if file.strip() == 'index.html':
        f = codecs.open(file, 'r', 'utf-8-sig')
        fajlliFizik = f.read()
        pergjigjja = b"""
HTTP/1.1 200 OK
Content-Type: text/html 
""" + fajlliFizik.encode("utf-8")

    else:
         pergjigjja = b"""
HTTP/1.1 404 Not Found
Content-Type: text/html

Ky fjall nuk ekziston
"""   
         
    clientSocket.sendall(pergjigjja)
    clientSocket.close()



# http://localhost:9999/fiek/ushtrimet/index.html
#GET /fiek/ushtrimet/index.html HTTP/1.1
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
#Accept-Language: en-US,en;q=0.7,sq;q=0.3
#Upgrade-Insecure-Requests: 1
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363
#Accept-Encoding: gzip, deflate
#Host: localhost:9999
#Connection: Keep-Alive

#pathi virtual duhet te jete i mapuar me pathin fizik

#/fiek/ushtrimet/index.html
#C:\fiek\ushtrimet\index.html
