import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter a message: ")

client.sendto(message.encode(), ("127.0.0.1", 5000))

data, address = client.recvfrom(1024)

print("Sentiment:", data.decode())

client.close()