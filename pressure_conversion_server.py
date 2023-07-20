import socket

def bar_to_atmosphere(bar_pressure):
    return bar_pressure * 0.986923

def main():
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket
    server_address = ('127.0.0.1', 8888)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening...")

    # Accept connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection accepted from {client_address[0]}:{client_address[1]}")

    # Receive pressure from the client
    data = client_socket.recv(1024)
    bar_pressure = float(data.decode())

    # Convert pressure to atmosphere-standard
    atmosphere_pressure = bar_to_atmosphere(bar_pressure)

    # Send the converted value to the client
    client_socket.send(str(atmosphere_pressure).encode())

    # Close the sockets
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
