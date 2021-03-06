import socket
import select
import errno
import sys
import time

HEADER_LENGTH=10
IP="127.0.0.1"
IP=socket.gethostname()
PORT=1238

to=time.time()
duration=20

my_username="Marc"
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((IP,PORT))
client_socket.setblocking(False)

username=my_username.encode('utf-8')
username_header=f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header+username)

while time.time()-to<duration:
    message="hi im "+my_username

    if message:
        message=message.encode('utf-8')
        message_header=f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header+message)
    try:
        while True:
            #receive things
            username_header=client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Client: Connection closed by the server")
                sys.exit()

            username_length=int(username_header.decode('utf-8').strip())
            username=client_socket.recv(username_length).decode('utf-8')

            message_header=client_socket.recv(HEADER_LENGTH)
            message_length=int(message_header.decode('utf-8').strip())
            message=client_socket.recv(message_length).decode('utf-8')

            print(f"Client: {username}>{message}")
    except IOError as e:
        if e.errno != errno.EAGAIN or e.errno != errno.EWOULDBLOCK:
            print("Client: Reading error",str(e))
            sys.exit()
        continue

    except Exception as e:
        print("Client: General error",str(e))
        sys.exit()


print("the client is done running")
