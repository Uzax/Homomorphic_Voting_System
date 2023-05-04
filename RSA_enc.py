from Crypto.PublicKey import RSA
from Crypto import Random


class RSA_ENC:
    PublicKey , PrivateKey = None , None

    def __init__(self):
        
        
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator) #generate pub and priv key
        self.PrivateKey = key
        self.PublicKey = key.publickey()

    
    def public_int(self):
        return self.PublicKey.n 

    def private_int(self):
        return self.PrivateKey.d
    
    def exponent(self):
        return self.PublicKey.e 
        