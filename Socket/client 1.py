import socket
import time


t0=time.time()
duration=5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '192.168.0.1'
port = 1234
s.connect((ip,port))

while time.time()-t0<duration:
    full_msg = ''
    while time.time()-t0<duration:
        print(time.time()-t0)
        msg = s.recv(8)
        if len(msg) <= 0:
            break
        full_msg += msg.decode("utf-8")

    if len(full_msg) > 0:
        print(full_msg)
