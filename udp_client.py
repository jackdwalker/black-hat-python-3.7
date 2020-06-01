import socket

target_host = '127.0.0.1'
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Allow client to also act as server and bind to itself
# https://stackoverflow.com/questions/37191612/issue-with-receiving-response-from-127-0-0-1-with-udp-client-in-python
client.bind((target_host, target_port))

# Send some data
client.sendto('AAABBBCCC'.encode(), (target_host, target_port))

# Receive some data
data, addr = client.recvfrom(4096)

print('data: {}'.format(data))
print('addr: {}'.format(addr))
