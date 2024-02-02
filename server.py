import socket
import threading

available = {"1.1.1.1", "2.2.2.2", "3.3.3.3"}
unavailable = set()

server_stopped = False # Flag to signal the server to stop

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Client says: {data}")

        # Check if the client wants to end the connection
        if data.lower() == "end":
            print("Client requested to end the connection.")
            break

        # Process client's request based on the provided logic
        x = data.split()

        if x[0].upper() == "ASK" and len(available) > 0:
            offered = available.pop()
            print(f"Offer {offered}")
            unavailable.add(offered)

        if len(x) > 1 and x[0].upper() == "RENEW" and x[1] in unavailable:
            print(f"RENEWED for {x[1]}")

        if len(x) > 1 and x[0].upper() == "RELEASE" and x[1] in unavailable:
            print(f"RELEASED for {x[1]}")
            unavailable.remove(x[1])
            available.add(x[1])

        if len(x) > 1 and x[0].upper() == "STATUS":
            if x[1] in available:
                print(f"{x[1]} AVAILABLE")
            elif x[1] in unavailable:
                print(f"{x[1]} ASSIGNED")
            else:
                print("Invalid.")

    # Close the connection with the client
    client_socket.close()

def stop_server():
    global server_stopped
    server_stopped = True
    server_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '127.0.0.1'  # localhost
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {host}:{port}")

# Create a new thread to listen for the "end" command and stop the server
stop_thread = threading.Thread(target=lambda: input("*Type 'end' in client to stop the server*") if not server_stopped else None)
stop_thread.start()

# Infinite loop to accept connections from clients
while not server_stopped:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
