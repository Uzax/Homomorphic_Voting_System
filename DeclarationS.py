import socket
import time
from RSA_enc import RSA_ENC
import Crypto.Random

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
s.bind(("", 9000))  # bind this port at this machine as a welcoming socket that will receive connection requests
s.listen(5)  # number of maximum queued requests
nonce = []
for i in range(3):
    print("Waiting for client ...")  # print on server terminal
    (c, a) = s.accept()  # accept request on the socket s
    print("Received connection from", a)  # print on server terminal ip of clint ip

    nC = int(c.recv(10000).decode())
    eC = int(c.recv(10000).decode())

    nonceEle = int.from_bytes(Crypto.Random.get_random_bytes(16), 'big')
    nonce.append(nonceEle)
    EncNonce = power_mod(nonceEle, eC, nC)
    c.send(str(EncNonce).encode())
    time.sleep(0.01)
    c.send(str(e).encode())  # send "greetings" to client
    time.sleep(0.01)
    c.send(str(n).encode())

print("Waiting for Untrusted Server ...")  # print on server terminal
(c, a) = s.accept()  # accept request on the socket s
print("Received connection from", a)  # print on server terminal ip of clint ip
EncVotes = int(c.recv(10000).decode())
print('EncVotes: ' + str(EncVotes))
c.close()
s.close()
print("Start....... Callculations.... \n")
DecVotes = power_mod(EncVotes, d, n)
for n in nonce:
    DecVotes = DecVotes / n
Result = prime_factors(int(DecVotes)) # factorize the result
my_dict = {i:Result.count(i) for i in Result} # convert array to dictionary
print(my_dict) # print dictionary
