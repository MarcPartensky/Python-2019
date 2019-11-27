import socket
import time


t0=time.time()
duration=5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ''
port = 1234
s.bind((ip, port))
s.listen(5)

while time.time()-t0<duration:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hey there!!!", "utf-8"))
    clientsocket.close()


print('server ended')
