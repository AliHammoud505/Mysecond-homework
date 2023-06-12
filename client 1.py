import socket

# Define the server address and port
host = "127.0.0.1"
port = 9999

# Create a TCP socket and connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print(f"Connected to {host}:{port}")

# Receive the quiz questions from the server and send answers
while True:
    question = client.recv(1024).decode()
    if not question:
        break
    print(question)
    answer = input()
    client.sendall(answer.encode())

# Receive the final score from the server and close the connection
final_score = client.recv(1024).decode()
print(final_score)
client.close()