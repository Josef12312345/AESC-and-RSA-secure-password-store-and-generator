import rsa

KEYSIZE = 4096    #4096 is the most perfer

class RSACipher:
    def __init__(self):
        self.pubkey = self.set_Public_key()
        self.privkey = self.set_Private_key()
    def __repr__(self):
        return self.pubkey
    def RSAEncry(self, raw):
        return rsa.encrypt(raw.encode("utf8"), self.pubkey)
    def RSAdecrpt(self, message):
        return rsa.decrypt(message, self.privkey).decode("utf8")  # would return a str 

    # Setting is use for decypher message, and use existant keys to encode message. Notice when encodding message private key
    #   is not important, we code ignore input.
    def key_generate(self, bitsize = KEYSIZE):
        (self.pubkey, self.privkey) = rsa.newkeys(bitsize)
    def set_Public_key(self, num1=5, num2=3):
        self.pubkey = rsa.key.PublicKey(num1,num2)
    def set_Private_key(self, num1=3727264081, num2=65537, num3=3349121513, num4=65063, num5=57287):
        self.privkey = rsa.key.PrivateKey(num1, num2, num3, num4, num5)
    

    # Return the key value
    def get_Public_key(self):
        return self.pubkey
    def get_Private_key(self):
        return self.privkey


    

