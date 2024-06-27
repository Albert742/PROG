import socket
import signal

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

def handle_timeout():
    print("Timeout occurred. Gracefully terminating client.")
    raise SystemExit

def signal_handler(signal, frame):
    print("Gracefully terminating client.")
    raise SystemExit

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
        print("Client started. Press Ctrl+C to terminate.")
        while True:
            message = input("Enter message: ")
            client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
            try:
                data, server_address = client_socket.recvfrom(1024)
                print(f"Received message from server: {data.decode()}")
            except socket.timeout:
                print("Timeout occurred. Retransmitting last message.")
                client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
                retransmitted_data, _ = client_socket.recvfrom(1024)
                print(f"Retransmitted message from server: {retransmitted_data.decode()}")

if __name__ == "__main__":
    run_client()