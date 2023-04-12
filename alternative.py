#Store sting
input_string1 = input("Please enter your text to alternate letters:\n")
#Empty string for interation
alt_string1 = ""

#interates over the length of the input
for i in range(len(input_string1)):

    #if i is odd at stores as a lowercase in the empty string
    if i % 2 == 1:
        alt_string1 += input_string1[i].lower()
        
    #if i is even it stores as an uppercase letter    
    else:
        alt_string1 += input_string1[i].upper()
#Prints the new string        
print(alt_string1)



#Second input for alternating words
input_string2 = input("\nPlease enter your text to alternate words:\n")
#Splits each world
split_string = input_string2.split()
#Empter string for interation
alt_string2 = ""

#If i is even it will become lower case and leave a space; if odd it becomes upper case and leaves a space
for i in range(len(split_string)):
    if i % 2 == 0:
        alt_string2 += split_string[i].lower() + " "
    else:
        alt_string2 += split_string[i].upper() + " "

#Joins the words back together - the space was needed to keep the words seperate
joined_string = "".join(alt_string2)
print(joined_string)


