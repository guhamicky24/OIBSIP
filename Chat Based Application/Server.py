### Chat based application by Micky Guha (Server file)
import socket
import threading

# List of all connected clients
clients = []

# Function to handle communication with clients
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    
    # Add the client to the list
    clients.append(client_socket)
    
    # Receive messages from the client
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Message from {client_address}: {message.decode('utf-8')}")
                # Broadcast message to all other clients
                broadcast_message(message, client_socket)
            else:
                # If message is empty, remove client
                remove_client(client_socket)
                break
        except:
            continue

# Function to broadcast message to all clients except the sender
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                continue

# Function to remove a client from the list of clients
def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Set up the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))  # Bind to all IP addresses on port 5555
    server.listen(5)
    print("Server started... Waiting for clients to connect.")
    
    while True:
        client_socket, client_address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
