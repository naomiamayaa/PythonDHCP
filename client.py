import socket
import threading

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Server says: {data}")

def send_messages(client_socket):
    while True:
        user_input = input("Enter your message: ")
        client_socket.send(user_input.encode())
        if user_input.lower() == 'exit':
            break

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'  # localhost
port = 12345
client_socket.connect((host, port))

# Create threads for sending and receiving messages
send_thread = threading.Thread(target=send_messages, args=(client_socket,))
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))

# Start the threads
send_thread.start()
receive_thread.start()

# Wait for both threads to finish
receive_thread.join()
send_thread.join()

# Close the connection
client_socket.close()
