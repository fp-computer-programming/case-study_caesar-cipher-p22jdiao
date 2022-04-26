

# Imports
from string import ascii_uppercase


# Functions
def cipher_key(shift):
    original_letters = ascii_uppercase
    shifted_letters = ascii_uppercase[int(shift):] + ascii_uppercase[:int(shift)]

    return dict(zip(original_letters, shifted_letters))


def shift_line(line, dict_key):
    new_line = ""
    for x in line:
        try:
            if x.isupper() == True:
                new_line += dict_key[x.upper()]
            else:
                new_line += dict_key[x.upper()].lower()
        except KeyError:
            new_line += x
    return new_line


def encrypt_message(filename, dict_key):
    old_file = open(filename,"r")
    new_file = open("new_file.txt","a")

    while True:
        o_line = old_file.readline()

        n_line = shift_line(o_line,dict_key)
        new_file.write(n_line+"\n")

        if len(o_line) == 0:
            break
    
    old_file.close()
    new_file.close()




# Main
user_file = input("Please enter a file to be encrypted: ")
shift_value = input("Please enter a shift value: ")

key = cipher_key(shift_value)

encrypt_message(user_file, key)
