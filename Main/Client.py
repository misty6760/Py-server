import socket

HOST = '127.0.0.1'
PORT = 2343

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))
print(f'Connected to {HOST}:{PORT}')

while True:
    message = input("Typing message (exit is stop): ")

    if message.strip() == '':
        continue
    if message == "exit":
        break

    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print("Server Answer: ", data.decode())

client_socket.close()