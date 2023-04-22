from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort)) #TCP three way hand shake is intiated
#at this line TCP connection is established
message = input('input lowercase sentence')
clientSocket.send(message.encode()) #directly dumps data into TCP connection
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('response:', modifiedMessage.decode())
clientSocket.close()