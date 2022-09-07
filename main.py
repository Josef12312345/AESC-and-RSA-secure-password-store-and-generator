import Encrpt_decrept    # this encrpt and decrypt files
import TextGenerator     # this generate password
import File_control      # Some level of file control (reduce code writing)
# tart = Encrpt_decrept.IniEncryp("Message_input.txt")

# continue_on = Encrpt_decrept.Encryption("Message_input.txt", "keys_public_file.txt")

# ending = Encrpt_decrept.Decypher("Encoding_file", "keys_store", "keys_private_file.txt")
#temp = TextGenerator.RandomGenerate(None, 1000, 1, True, True, True)

#### example of use 

# Password_generate
Password_generator = TextGenerator.RandomGenerate("...|:)|..li..", 13, 20, True, False, True)
password_sets = Password_generator.generator()
message = ""
for str in password_sets:
    message = message + str + "\n"


# Initial Encryption
# There is a default name for generated files, change the name of files is an option
file = File_control.FileControl()    
file.write_message_file(message)
Initial_encrypt = Encrpt_decrept.IniEncryp("Message_file.txt")   # Again there is an defualt file name

# Now four more files generated

# Encryption (modification of message)
message = message + "\nIs there a way to break RSA encryption???"
file.write_message_file(message)
encrypt = Encrpt_decrept.Encryption()   # Since we use the default name in FileControl(), therefore
#   We don't need to add anything in Encryption()


# Decypher
# here we need to delete the original message file (otherwise we won't see the result)
Encrpt_decrept.Decypher()

# Result shown here is:

# q3m|:)|uhlinF
# 3GG|:)|JglixH
# M2w|:)|Axli94
# ICb|:)|wcli39
# GuH|:)|rHliNn
# 7tf|:)|rSliat
# YbG|:)|akliA1
# B0T|:)|mVliOr
# 5EQ|:)|W2liAy
# fEa|:)|2BliwS
# 3b6|:)|OwlidD
# OJv|:)|8ZliLw
# 6fH|:)|lzliLc
# 9W1|:)|OTlizt
# AX3|:)|JEliGY
# YcD|:)|HsliRo
# W9J|:)|JtliCM
# a2g|:)|VDliSr
# xHX|:)|FEli50
# wGT|:)|eOliBU

# Is there a way to break RSA encryption???


#print(temp.generator()[0])

##### Key takeaway (save you time) !!!
# All you need to keep is: 
#  1. Encoding_file
#  2. keys_private_file.txt
#  3. keys_store

# These three file is all you need for this program to decryper. 
# Note if you want to modify faster you might want to keep keys_public_file.txt
#   however it is not necessary.

# Best way to keep file safe is to put it in some usb hard drive that no one
#   can access but you. 