import socket

def main():
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server address
    server_address = ('127.0.0.1', 8888)

    # Connect to the server
    client_socket.connect(server_address)

    # Get pressure input from the user
    bar_pressure = float(input("Enter pressure in bar: "))

    # Send the pressure to the server
    client_socket.send(str(bar_pressure).encode())

    # Receive converted pressure from the server
    data = client_socket.recv(1024)
    atmosphere_pressure = float(data.decode())

    # Display the converted pressure
    print(f"Pressure in atmosphere-standard: {atmosphere_pressure} atm")

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
