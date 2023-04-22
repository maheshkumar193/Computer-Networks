from distutils.command.clean import clean
from pydoc import cli
from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('input lowercase sentence')
# IP address and socket port for client are choosen by OS and attached to packet before sending
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('from server:', serverAddress, ' response:', modifiedMessage)
clientSocket.close()