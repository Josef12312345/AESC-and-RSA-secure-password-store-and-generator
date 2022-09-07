import datetime

class FileControl:
    def __init__(self, Message_file = "Message_file.txt", Encoding_file ="Encoding_file", keys_private_file = "keys_private_file.txt", keys_public_file = "keys_public_file.txt", keys_store = "keys_store", log_file = "log.txt"):
        self.Mfile = Message_file
        self.Efile = Encoding_file
        self.keys_private_file = keys_private_file
        self.keys_public_file = keys_public_file
        self.log_file = log_file
        self.keys_store = keys_store
    
    # Read and Write of the file
    def read_message_file(self):
        file = open(self.Mfile, "r")
        log = open(self.log_file, "a")
        log.write("\n------------------------------- \n Read the file" + self.Mfile + " at " + str(datetime.datetime.now()))
        content = file.read()
        log.close()
        file.close()
        return content
    def write_message_file(self, content):
        file = open(self.Mfile, "w")
        log = open(self.log_file, "a")
        log.write("\n------------------------------- \n Write the file" + self.Mfile + " at " + str(datetime.datetime.now()))
        file.write(content)
        log.close()
        file.close()
    def read_Encoding_file(self):
        file = open(self.Efile, "rb")
        log = open(self.log_file, "a")
        log.write("\n------------------------------- \n Read the file" + self.Efile + " at " + str(datetime.datetime.now()))   
        content = file.read()
        file.close()
        log.close()
        return content
    def write_Encoding_file(self, content):
        file = open(self.Efile, "wb")
        log = open(self.log_file, "a")
        log.write("\n------------------------------- \n Write the file" + self.Efile + " at " + str(datetime.datetime.now()))   
        file.write(content)
        log.close()
        file.close()
    def read_keys_public_file(self):
        file = open(self.keys_public_file, "r")
        log = open(self.log_file, "a")
        log.write("\n------------------------------- \n Read the file" + self.keys_public_file + " at " + str(datetime.datetime.now()))   
        content = file.read()
        log.close()
        file.close()
        return content
    def write_keys_public_file(self, content):
        file = open(self.keys_public_file, "w")
        log = open(self.log_file, "a")
        log.write("\n------------------------------- \n Write the file" + self.keys_public_file + " at " + str(datetime.datetime.now()))  
        file.write(content)
        log.close()
        file.close()

    def read_keys_private_file(self):
        file = open(self.keys_private_file, "r")
        log = open(self.log_file, "a")
        log.write("\n------------------------------- \n Read the file" + self.keys_private_file + " at " + str(datetime.datetime.now()))   
        content = file.read()
        log.close()
        file.close()
        return content
    def write_keys_private_file(self, content):
        file = open(self.keys_private_file, "w")
        log = open(self.log_file, "a")
        log.write("\n------------------------------- \n Write the file" + self.keys_private_file + " at " + str(datetime.datetime.now()))  
        file.write(content)
        log.close()
        file.close()

    def read_keys_store_file(self):
        file = open(self.keys_store, "rb")
        log = open(self.log_file, "a")
        log.write("\n------------------------------- \n Read the file" + self.keys_store + " at " + str(datetime.datetime.now()))
        content = file.read()
        log.close()
        file.close()
        return content
    def write_keys_store_file(self, content):
        file = open(self.keys_store, "wb")
        log = open(self.log_file, "a")
        log.write("\n------------------------------- \n Write the file" + self.keys_store + " at " + str(datetime.datetime.now()))
        file.write(content)
        log.close()
        file.close()

    # Notice this log will only record the date time of modification, not the value of modification.
    def print_log(self):
        log = open(self.log_file, "r")
        print(log.read())
        log.close()

    def print_file_names(self):
        print(self.Efile + "  |  " + self.Mfile + "  |  " + self.keys_file + "  |  " + self.log_file)


    def set_names(self, Message_file = None, Encryption_file = None, Key_file = None):
        if Message_file is not None:
            self.Mfile = Message_file
        if Encryption_file is not None:
            self.Efile = Encryption_file
        if Key_file is not None:
            self.keys_file = Key_file