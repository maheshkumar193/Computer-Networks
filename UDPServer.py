from socket import *
serverName = '127.0.0.1'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print('server is ready to recieve')
while True:
  message, clientAddress = serverSocket.recvfrom(2048)
  message = message.decode()
  print('client from:',clientAddress,' client sent:', message)
  modifiedMessage = message``.upper()
  serverSocket.sendto(modifiedMessage.encode(), clientAddress)
  # IP address and socket port for server are choosen by OS and attached to packet before sending