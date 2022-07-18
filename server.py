import socket
import threading # Create multiple threads within one Python program  ( Seperate code out so it not waiting for order code to finish before it able to execute ) multithread sustains the threads or the clients connected to it in a Python application.


HEADER = 64
PORT = 5050
# SERVER = "172.16.2.61"  # I run this as my local network 
# Or We can do this 
SERVER = socket.gethostbyname(socket.gethostname()) # Auto get IP 
ADDR = (SERVER, PORT) # Bining it together 
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"# When the client disconnect it will tell the server 



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # what type of IP | Streaming data to socket
server.bind(ADDR)



def handle_client(conn, addr):
    # handle individul connection between the client and the server 
    print(f"NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            # Send from server to the client 
            conn.send("Message received".encode(FORMAT))

    conn.close()


def start():
    # handing connection and distribute those 
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")

print("[STARTING] server is starting...") 
start()