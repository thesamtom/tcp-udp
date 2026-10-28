import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 5000))

print("Server waiting...")

data, address = server.recvfrom(1024)
msg = data.decode().lower()

positive = ["good", "happy", "great", "excellent", "love", "nice"]
negative = ["bad", "sad", "worst", "hate", "poor", "terrible"]

p = 0
n = 0

for word in msg.split():
        if word in positive:
            p += 1
        if word in negative:
            n += 1

if p > n:
        result = "Positive"
elif n > p:
        result = "Negative"
else:
        result = "Neutral"

print("Message:", msg)
print("Sentiment:", result)

server.sendto(result.encode(), address)

server.close()