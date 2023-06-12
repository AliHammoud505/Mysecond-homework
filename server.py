import socket
import threading

# Define the quiz questions and answers
quiz = {
    "1+1": "2",
    "2+1": "3",
    "3+2": "5",
    "2+3": "5",
}

# Define a function to handle client connections
def handle_client(conn, addr, scores):
    print(f"New connection from {addr}")

    # Send the quiz questions to the client
    for question in quiz.keys():
        conn.sendall(question.encode())
        answer = conn.recv(1024).decode()

        # Check the answer and update the score
        if answer == quiz[question]:
            scores[addr] += 1

    # Send the final score to the client
    final_score = f"Your final score is: {scores[addr]}/{len(quiz)}"
    conn.sendall(final_score.encode())
    conn.close()
    print(f"Connection from {addr} closed")


# Define the main function
def main():
    # Create a TCP socket and bind it to a port
    host = "127.0.0.1"
    port = 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Server listening on {host}:{port}")

    # Keep track of the scores for each client
    scores = {}

    # Accept client connections and start a new thread for each client
    while True:
        conn, addr = server.accept()
        scores[addr] = 0
        thread = threading.Thread(target=handle_client, args=(conn, addr, scores))
        thread.start()


if __name__ == "__main__":
    main()