import socket
import time

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

def handle_client(client_socket):
    data = None  # Initialize data variable
    while True:
        try:
            data, client_address = client_socket.recvfrom(1024)
            print(f"Messaggio ricevuto da: {client_address}: {data.decode()}")
            client_socket.sendto(data, client_address)
            time.sleep(2)  # Simulazione di un ritardo di 2 secondi
        except socket.timeout:
            if data is not None:  # Check if data is defined
                print("Timeout Avvenuto. Ritrasmetto l'ultimo messaggio.")
                client_socket.sendto(data, client_address)
            else:
                print("Nessun messaggio da ritrasmettere.")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.settimeout(5)  # Set timeout for receiving messages
    while True:
        handle_client(server_socket)

