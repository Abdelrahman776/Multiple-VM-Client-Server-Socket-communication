import socket
import threading

PORT=5050
SERVER_IP="192.168.100.4" 
#print(SERVER_IP)
ADDR = (SERVER_IP, PORT)
FORMAT = "utf-8"
msg_length=1024
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] with {addr[0]} ")

    connected = True
    while connected:
        msg = conn.recv(msg_length).decode(FORMAT)
        if not msg:
            break

        if msg == DISCONNECT_MESSAGE:
            connected = False
            continue
        

        if addr[0]=="192.168.100.5":   
            print(f"Client1 : {msg}")
            server_msg=input("what is the Server response : ")
            conn.send(f"The Server respond to\"{msg}\" : {server_msg}".encode(FORMAT))

        if addr[0]=="192.168.100.6": 
            print(f"Client2 : {msg}")
            server_msg=input("what is the Server response : ")
            conn.send(f"The Server respond to\"{msg}\" : {server_msg}".encode(FORMAT))

    conn.close()


def start():
    print('[SERVER STARTED]')
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start()