import socket
import threading

clients = {}

def handle_client(client_socket, address):
    client_name = f"Client {len(clients) + 1}"
    clients[client_socket] = client_name
    
    # Notify everyone about new connection
    broadcast(f"(Server): {client_name} has joined", None)
    
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            # Format message with client name
            formatted_msg = f"({client_name}): {message}"
            print(formatted_msg)  # Show on server console
            broadcast(formatted_msg, client_socket)
    except:
        pass
        
    # Client disconnected
    print(f"(Server): {client_name} disconnected")
    broadcast(f"(Server): {client_name} has left", None)
    
    del clients[client_socket]
    client_socket.close()

def broadcast(message, sender_socket):
    for client in list(clients.keys()):
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                del clients[client]
                
def main():
    server_address = ('localhost', 8833)    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print(f'[ LISTENING ] Server listening on {server_address[0]}:{server_address[1]}')
    
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
        print(f'[ ACTIVE CONNECTIONS ]: {len(clients)}')

if __name__ == '__main__':
    print('[ STARTING ] Server is starting...')
    main()
