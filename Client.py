import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))
print("Connection Established")

sending_message = "send file"
client_socket.send(sending_message.encode('utf-8'))

received_message = client_socket.recv(1024)

file = received_message.decode('utf-8')
recieved_message = open('Recieved_file.txt' , 'wt')
recieved_message.write(file)

recieved_message.close()
client_socket.close()
