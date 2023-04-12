size = int(input("How many rows of stars would you like?\n"))+1 # Range does not include the last number so +1 is needed
for i in range(1,size): 
    print(i*"*") # Prints "*" up to the desired number of times