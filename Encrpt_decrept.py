import File_control
import TextGenerator
import AESCipher
import RSAencrept

# Input "Message file.txt" would generate 4 file they are: 
#   1. Encoding_file.txt
#   2. "keys_store"  which is the encrpted AES keys by using RSA that is for extra security.
#   3. "keys_private_file.txt"   it is the private RSA key, you should keep it very secrete, expose it would make password easy to break
#   4. "keys_public_file.txt"    it is the public RSA key, you could expose it.

# And extra add on is the "log.txt" which produce the record of when writing and reading happen. 


KEYSIZE = 100

def encrpt_message(key, message_content):
    AESCencrptor = AESCipher.AESCipher(key)
    return AESCencrptor.encrypt(message_content)

def get_pub_key(public_key):
    content = public_key
    content = content.split("PublicKey(", 1)[1]
    [val1, val2] = content.split(",", 1)
    c_val1 = int(val1)
    c_val2 = int(val2[:-1])
    return c_val1, c_val2

def get_private_key(private_key):
    content = private_key
    content = content.split("PrivateKey(", 1)[1] 
    [val1, val2, val3, val4, val5] = content.split(",", 4)
    c_val1 = int(val1)
    c_val2 = int(val2)
    c_val3 = int(val3)
    c_val4 = int(val4)
    c_val5 = int(val5[:-1])
    return c_val1, c_val2, c_val3, c_val4, c_val5

class IniEncryp:
    def __init__(self, message_file = "Message_file.txt"):
        file = File_control.FileControl(message_file)
        self.message_content = file.read_message_file()
        temp = TextGenerator.RandomGenerate(None, KEYSIZE, 1, True, True, True)
        self.key = temp.generator()[0]
        output_message = encrpt_message(self.key, self.message_content)
        Encrepted_key, privkey, pubkey = self.encrpt_key()
        file.write_Encoding_file(output_message)
        file.write_keys_store_file(Encrepted_key)
        file.write_keys_private_file(str(privkey))
        file.write_keys_public_file(str(pubkey))
        print(".... Initial Encryption completed ....")
    def encrpt_key(self):
        RSAencrptor = RSAencrept.RSACipher()
        RSAencrptor.key_generate()
        Encrepted_key = RSAencrptor.RSAEncry(self.key)
        privkey = RSAencrptor.get_Private_key()
        pubkey = RSAencrptor.get_Public_key()
        return Encrepted_key, privkey, pubkey

# We still use the old RSA encryption public and private key, this way we don't need to waste time to generate new
#   RSA private or public key
class Encryption:
    def __init__(self, message_file = "Message_file.txt", public_key_file = "keys_public_file.txt"):
        file = File_control.FileControl(message_file, keys_public_file = public_key_file)
        self.message_content = file.read_message_file()
        temp = TextGenerator.RandomGenerate(None, KEYSIZE, 1, True, True, True)
        self.key = temp.generator()[0]
        output_message = encrpt_message(self.key, self.message_content)
        
        #Encryption of key process
        RSAencrptor = RSAencrept.RSACipher()
        public_key = file.read_keys_public_file()
        val1, val2 = get_pub_key(public_key)
        RSAencrptor.set_Public_key(val1, val2)
        Encrepted_key = RSAencrptor.RSAEncry(self.key)
        file.write_Encoding_file(output_message)
        file.write_keys_store_file(Encrepted_key)

        print("... Encryption Process completed ... ")


class Decypher:
    def __init__(self, encoding_file = "Encoding_file", keys_store = "keys_store", keys_private_file = "keys_private_file.txt"):
        file = File_control.FileControl(Encoding_file=encoding_file, keys_store=keys_store, keys_private_file=keys_private_file)
        
        # Get the private key of RSA
        private_keys = file.read_keys_private_file()
        val1, val2, val3, val4, val5 = get_private_key(private_keys)
        RSAdecyp = RSAencrept.RSACipher()
        RSAdecyp.set_Private_key(val1, val2, val3, val4, val5)

        # decypher the AESC file
        key_val = file.read_keys_store_file()
        key = RSAdecyp.RSAdecrpt(key_val)

        # get the actual message
        AESCencrptor = AESCipher.AESCipher(key)
        enigma = file.read_Encoding_file()
        message = AESCencrptor.decrypt(enigma)
        file.write_message_file(message)
        
        print("... Decypher process completed ... ")

        