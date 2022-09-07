# Some many txt files must do some clean up for testing and generating

import os

remove_file = ["Encoding_file", "keys_private_file.txt", "keys_public_file.txt", "keys_store", "Message_file.txt"]
for file in remove_file:
    os.remove(file)