import socket

client = socket.socket()
client.connect(("127.0.0.1", 12345))

# Enter client name
name = input("Enter your name: ")
client.send(name.encode())

print("\nConnected to server")

# Receive questions
questions = client.recv(4096).decode()
print(questions)

# Enter answers
answers = []

for i in range(5):
    ans = input("Enter answer (A/B): ")
    answers.append(ans.upper())

# Send answers
client.send(",".join(answers).encode())

# Receive score
score = client.recv(1024).decode()
print("\nStudent:", name)
print("Final Score:", score, "/ 5")

client.close()