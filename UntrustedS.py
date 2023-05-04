import socket
import time
from RSA_enc import RSA_ENC

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


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

myIP = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a socket with ipv4 hence the first parameter
                                                       # and TCP connection hence SOCK_STREAM
s.bind(("", 8000))  # bind this port at this machine as a welcoming socket that will receive connection requests
s.listen(5)  # number of maximum queued requests

fin = 1 
for i in range(3):
    print("Waiting for client ...")  # print on server terminal
    (c, a) = s.accept()  # accept request on the socket s
    print("Received connection from", a)  # print on server terminal ip of clint ip
    c.send(str(e).encode())  # send "greetings" to client
    time.sleep(0.01)
    c.send(str(n).encode())
    time.sleep(0.01)
    v = int(c.recv(10000).decode())
    print('Double Encrypted Vote: ' + str(v))
    v_dec = power_mod(v, d, n) #decryption between client and Untrusted 
    print('EncVote: ' + str(v_dec))
    fin *= v_dec
    #c.close()

s.close()



time.sleep(0.5)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
DeclarationIP = socket.gethostbyname(socket.gethostname()) # change IP if not running in the same machine
s.connect((DeclarationIP, 9000))  # connect to the server with ip address of server
                             # on port 9000
                             # perform 3-way handshake

s.send(str(fin).encode()) # send
print('Votes multiplied together: ' + str(fin))
s.close()