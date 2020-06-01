import socket

target_host = 'www.google.com'
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send some data
# Note: the encode() function will use UTF-8 by default. Being specific despite
#   this will improve readability for those who are not aware of this
#   though.
client.send('GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'.encode('UTF-8'))

# Receive some data
# Note: the decode() function will also use UTF-8 by default.
response = client.recv(4096).decode('UTF-8')

print(response)
