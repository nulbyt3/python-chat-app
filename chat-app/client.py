import socket
import threading

# Global variables
client_socket = None
client_name = 'Unknown'

def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                # Clear current input line and print message
                print(f"\r{message}\n(You): ", end='', flush=True)
        except:
            print("\r(System): Disconnected from server")
            client_socket.close()
            break

def send_message():
    while True:
        try:
            message = input("(You): ")
            if message.strip():  # Only send non-empty messages
                client_socket.send(message.encode('utf-8'))
        except:
            print("(System): Failed to send message")
            break

def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect(('localhost', 8833))
        print("Connected to server!")
        
        # Start threads
        threading.Thread(target=receive_message, daemon=True).start()
        send_message()  # Run in main thread
        
    except ConnectionRefusedError:
        print("(System): Could not connect to server")
    finally:
        client_socket.close()

if __name__ == '__main__':
    start_client()
