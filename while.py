sum = 0 # stores the sum of the user inputs
iterations = 0 # To store the divisor of the average

while True: # Infinite loop to keep asking for an input below
    user_number = int(input("Please enter a number (Type -1 to stop): "))
    if user_number != -1:
        sum += user_number # adds the number to sum
        iterations += 1 # adds up the number of loops
    else:
        mean = sum/iterations # calculation for the mean
        print(f"The mean of your numbers is {mean}")
        break # Stops the loop
   