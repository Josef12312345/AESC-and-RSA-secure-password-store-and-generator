import random
import string

class RandomGenerate:
    # format:
    # l.....K  -> l12345k 
    def __init__(self, acceptable_format=None, length=10, generated_number = 10, uppercase=False, special_character=False, number=False):
        if acceptable_format is not None:
            assert(len(acceptable_format) == length) 
        self.formating = acceptable_format
        self.uppercase = uppercase
        self.special_character= special_character
        self.number = number
        self.generated_number = generated_number
        self.length = length

    def generate_list(self, len, upper, special, num):
        str_sets = string.ascii_lowercase
        if(upper):
            str_sets += string.ascii_uppercase
        if(special):
            str_sets += string.punctuation
        if(num):
            str_sets += string.digits
        return "".join(random.choice(str_sets) for i in range(len))

    def generator(self):
        random_pass = []
        for i in range(self.generated_number):
            if self.formating is not None:
                index = 0
                replace_loc = []
                char_lst = []
                for element in self.formating:
                    char_lst.append(element)
                    if(element == '.'):
                        replace_loc.append(index)
                    index += 1
                replace_len = len(replace_loc)
                random_lst = self.generate_list(replace_len, self.uppercase, self.special_character, self.number)
                index_2 = 0
                for j in replace_loc:
                    char_lst[j] = random_lst[index_2]
                    index_2 += 1
                random_pass.append("".join(char_lst))
            else:
                char_lst = self.generate_list(self.length, self.uppercase, self.special_character, self.number)
                random_pass.append("".join(char_lst))
        return random_pass


    
        
