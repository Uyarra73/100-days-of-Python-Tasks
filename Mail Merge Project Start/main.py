#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open("Input/Letters/starting_letter.txt") as letter:
#     text = letter.read()
#     print(text)

with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    text = letter.read()

for name in name_list:
    selected_name = name.strip()
    new_letter = text.replace("[name]", selected_name)

    with open(f"Output/ReadyToSend/{selected_name}.docx", mode="w") as completed_letter:
        completed_letter.write(new_letter)


