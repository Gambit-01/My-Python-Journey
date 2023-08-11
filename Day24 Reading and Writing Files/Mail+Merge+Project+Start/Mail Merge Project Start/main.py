#TODO: Create a letter using starting_letter.txt 
with open("Mail Merge Project Start/Input/Names/invited_names.txt", mode = "r") as namelist:
    people = namelist.readlines()
    # print(people)

with open("Mail Merge Project Start/Input/Letters/starting_letter.txt", mode = "r") as invite:
    letter = invite.read()    
    for friend in people:
        person = friend.strip("\n")
        invitation_letter = letter.replace("[Name]",f"{person},")  
        with open(f"Mail Merge Project Start/Output/letter_for_{person}.txt" , mode = "w") as welcome:
            welcome.write(invitation_letter)
        
   
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp