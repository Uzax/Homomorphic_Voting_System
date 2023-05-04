import socket  # importing socket programming library
from RSA_enc import RSA_ENC
import time

key = RSA_ENC()
d = key.private_int()
n = key.public_int()
e = key.exponent()

def power_mod(b, e, m):
    x = 1
    while e > 0:
        b, e, x = (
            b * b % m,
            e // 2,
            b * x % m if e % 2 else x
        )
    return x

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a socket with ipv4 hence the first parameter
# and TCP connection hence SOCK_STREAM
myIP = socket.gethostbyname(socket.gethostname())
DeclarationIP = socket.gethostbyname(socket.gethostname()) # change IP if not running in the same machine
UntrustedIP = socket.gethostbyname(socket.gethostname()) # change IP if not running in the same machine
s.connect((DeclarationIP, 9000))  # connect to the server with ip address of server
                             # on port 9000
                             # perform 3-way handshake

s.send(str(n).encode())
time.sleep(0.01)
s.send(str(e).encode())
Encnonce = int(s.recv(10000).decode())
nonce = power_mod(Encnonce, d, n)

e1 = int(s.recv(10000).decode())  # receive data from server
n1 = int(s.recv(10000).decode())  # receive data from server
s.close()

print('Khalid = 2, Zayed = 3, Omar = 5')
Vote = int(input("Enter Your Vote: ")) # TODO: add your vote here
Vote *= nonce
EncVote = power_mod(Vote, e1, n1)
print('EncVote: ' + str(EncVote))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a socket with ipv4 hence the first parameter
s.connect((UntrustedIP, 8000))  # connect to the server with ip address of server
e2 = int(s.recv(10000).decode())  # receive data from server
n2 = int(s.recv(10000).decode())  # receive data from server
DEncVote = power_mod(EncVote, e2, n2)
print('Double Encrypted Vote: ' + str(DEncVote))

s.send(str(DEncVote).encode())
print("SENT")
s.close()
