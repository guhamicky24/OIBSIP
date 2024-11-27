### Chat based application by Micky Guha (Client file)

import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Received: {message.decode('utf-8')}")
        except:
            print("Connection closed.")
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input()  # Take user input for sending messages
        if message:
            client_socket.send(message.encode('utf-8'))

# Set up the client
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))  # Connect to the server on localhost and port 5555
    
    # Start a thread to listen for incoming messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    # Start a thread to send messages to the server
    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

if __name__ == "__main__":
    start_client()
