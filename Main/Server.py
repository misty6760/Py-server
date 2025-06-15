import socket

HOST = '127.0.0.1'
PORT = 2343

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen()
print(f'The server is waiting on {HOST}:{PORT}...')

while True:
    client_socket, client_address = server_socket.accept()
    print(f'The client is connected...')

    while True:
        data = client_socket.recv(1024)

        if not data:
            print(f'The client is disconnected: {client_address}...')
            break

        print('Take message: ', data.decode())
        client_socket.sendall(data)

    client_socket.close()