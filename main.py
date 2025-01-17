#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from importlib.resources import contents

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# My Solution
# (1)   assign the name of the file (invited_names.txt) to a variable called invited_names_list. Use the method readline()

import string
invited_names_file = "input/names/invited_names.txt"    # Assign filepath to invited_names.txt to a variable
starting_letter_file = "input/letters/starting_letter.txt"  # Assign filepath to starting_letter.txt to a rariable
storage_folder = "output/ReadyToSend"   # Assign filepath to ReadyToSend folder to a variable


with open(invited_names_file, "r") as file: # Open invited_names_file
    invited_names_list = file.readlines()   # Convert content in invited_names_file to a list of strings

    with open(starting_letter_file, "r") as file:   # Open starting_letter file
        starting_letter = file.read()
        for name in invited_names_list:     # For each name in invited_names_list
            new_name = str(name)            # Convert name to string
            name_to_write = new_name.strip()    # Remove the return character from each name in a list
            invited_name_letter = starting_letter.replace("[name]", name_to_write)  # Replace placeholder with each name
            with open(f"{storage_folder}/letter_for_{name_to_write}.txt", mode="w") as file:
                file.write(invited_name_letter) # Write and save each file