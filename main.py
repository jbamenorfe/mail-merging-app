"""This program sends a similar email to a list of recipients. It replaces a placeholder with in the salutation - [name] with each recipient's name. By JBAmenorfe on 17/01/2025"""
invited_names_file = "./input/names/invited_names.txt"    # Assign filepath to invited_names.txt to a variable
starting_letter_file = "./input/letters/starting_letter.txt"  # Assign filepath to starting_letter.txt to a rariable
storage_folder = "./output/ReadyToSend"   # Assign filepath to ReadyToSend folder to a variable


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