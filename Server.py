import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port_number = 8000

server_socket.bind(('localhost', port_number))
server_socket.listen()
client_socket, client_address = server_socket.accept()

print("Connection Established !!")
received_message = client_socket.recv(1024)
print(f"Client: {received_message.decode('utf-8')}")

if received_message.decode('utf-8') == 'send file':
    file = open('Sending_file.txt' , 'r')
    sending_message = file.read()
    client_socket.send(sending_message.encode('utf-8'))

server_socket.close()
