

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
            if x.isupper() == True: # Because the cipher_key() function returns only the capital letters
                new_line += dict_key[x.upper()] # If the original letter is a upper case letter then just use the corresponding key
            else: # If the original letter is a lowercase letter, then change the replacing key into a lowercase letter
                new_line += dict_key[x.upper()].lower()
        except KeyError: # The key function does not contain any symbols, and there is no need to replace a symbol
            new_line += x # So just simply use the original symbol, which is x
    return new_line


def encrypt_message(filename, dict_key):
    old_file = open(filename,"r") # Use reading mode to open the original file
    new_file = open("new_file.txt","a") # Use append mode for the moderating one.

    while True:
        o_line = old_file.readline() # Go through the original file line by line

        n_line = shift_line(o_line,dict_key) # Create the shifted version of the line
        new_file.write(n_line+"\n") # Add the shifted line into the new file

        if len(o_line) == 0: # Once the .readline() reaches the end, the length of the line will be zero, then break the while loop
            break
    
    old_file.close()
    new_file.close()




# Main
user_file = input("Please enter a file to be encrypted: ")
shift_value = input("Please enter a shift value: ")

key = cipher_key(shift_value)

encrypt_message(user_file, key)
