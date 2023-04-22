from socket import *
serverName = '127.0.0.1'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) # welcome socket
serverSocket.bind((serverName, serverPort))
serverSocket.listen(5) # wait and listen for some client to request for connection
# 5 means max no.of queued connections
print('server is ready to recieve')
while True:
  connectionSocket, clientAddress = serverSocket.accept() # TCP 3 way hand shake is complete
  # connectionSocket => dedicated socket for clientAddress client for transfer of reliable data
  message, clientAddress = connectionSocket.recvfrom(2048)
  message = message.decode()
  print('request:', message)
  modifiedMessage = message.upper()
  connectionSocket.send(modifiedMessage.encode())
  connectionSocket.close()
  # IP address and socket port for server are choosen by OS and attached to packet before sending
