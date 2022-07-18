# multi client connect to server 
import socket


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


# After we connect with the server We need to send something to the server 
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # Get message from server 
    print(client.recv(2048).decode(FORMAT))

# send("Hello, World")
# send("You are great ")
# send("I believe in You")
# send(DISCONNECT_MESSAGE)

# ______________________________Connect with multiple client ____________________________________________# 

send("Hello, World")
input()
send("You are great ")
input()
send("I believe in You")
send(DISCONNECT_MESSAGE)