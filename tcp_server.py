import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5)

print('[*] Listening on {}:{}'.format(bind_ip, bind_port))

# This is our client handling thread
# Note: Remember to decode the incoming request, and encoding the outgoing ACK
#   packet
def handle_client(client_socket):
    # Print out what the client sends
    request = client_socket.recv(1024).decode()

    print('[*] Received: {}'.format(request))

    # Send back a packet
    client_socket.send('ACK:'.encode())
    client_socket.close()

while True:
    client, addr = server.accept()
    print('[*] Accepted connection from: {}:{}'.format(addr[0], addr[1]))

    # Spin up our client thread to handle incoming data
    client_handler = threading.Thread(target = handle_client, args = (client, ))
    client_handler.start()