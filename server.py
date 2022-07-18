import socket
import threading # Create multiple threads within one Python program  ( Seperate code out so it not waiting for order code to finish before it able to execute )

PORT = 5050
# SERVER = "172.16.2.61"  # I run this as my local network 
# Or We can do this 
SERVER = socket.gethostbyname(socket.gethostname()) # Auto get IP 
print(SERVER)