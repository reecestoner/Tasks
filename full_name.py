full_name = input("Please enter your full name: ")

if len(full_name) == 0:  # Creating if statement if they input no name
    print("You haven't entered anything. Please enter your full name.")
elif len(full_name)<4:    # If they only typed less than 3 characters; lines seperated so its easier for the user to read
    print("""You have entered less than 4 characters. 
Please make sure that your have entered your name and surname.""")
elif len(full_name)>25:  # If name is too long
    print("""You have entered more than 25 characters. 
Please make sure that you have only entered your full name.""")
else:
    print("Thanks for entering your name!")
