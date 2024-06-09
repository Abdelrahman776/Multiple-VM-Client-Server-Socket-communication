import socket


SERVER_IP = "192.168.100.4"
PORT = 5050
ADDR = (SERVER_IP, PORT)
FORMAT = "utf-8"
msg_length=2048
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)

def receive (conn):
    input("press enter to receive the respond")
    msg=conn.recv(msg_length).decode(FORMAT)
    print(f"{msg}")

def start():
    connection = connect()
    print("Connection between server and client 1 is established")
    while True:
        msg = input("Type a message to the Server(q for dissconect): ")

        if msg == 'q':
            break

        send(connection, msg)
        receive(connection)
        
        

    send(connection, DISCONNECT_MESSAGE)
    print('Disconnected')


start()