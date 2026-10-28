import socket

server = socket.socket()
server.bind(("127.0.0.1", 12345))
server.listen(1)

print("Waiting for client...")
conn, addr = server.accept()
print("Client connected")

# Receive client name
name = conn.recv(1024).decode()
print("Client Name:", name)

# Questions
questions = """
1. Full form of TCP?
A. Transmission Control Protocol
B. Transfer Control Protocol

2. Which is connection-oriented?
A. UDP
B. TCP

3. Localhost IP address?
A. 127.0.0.1
B. 192.168.1.1

4. Which device connects networks?
A. Switch
B. Router

5. Which protocol is used for web browsing?
A. HTTP
B. FTP
"""

answers = ["A", "B", "A", "B", "A"]

# Send questions
conn.send(questions.encode())

# Receive answers
data = conn.recv(1024).decode()
client_answers = data.split(",")

# Calculate score
score = 0
for i in range(5):
    if client_answers[i].strip().upper() == answers[i]:
        score += 1

print("Client Answers:", client_answers)
print("Final Score of", name, ":", score, "/ 5")

# Send score
conn.send(str(score).encode())

conn.close()
server.close()