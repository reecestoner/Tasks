while True:
    file = None
    try:
        value1 = float(input("Enter your first number:\n")) #Input any number
        if value1 == int(value1): # The input converts from a float to an integer if it has no decimal places
            value1 = int(value1)
            
        # Record the required operation
        op = input("How would you like to operate on this? (Enter x / + -)\n")

        # If the input isn't an operation an exception will be returned
        if op != 'x' and op!='/' and op!='+'and op!='-': 
             raise Exception("Invalid input - non-operator entered. Please enter either x / + or - ")
        
        
        # Input a number, if its not a float it converts to an integer
        value2 = float(input("Enter your second number:\n"))
        if value2 == int(value2):
             value2 = int(value2)

        # Calculates the answer for the operation entered
        if op == "x":
            calculation = value1 * value2
        elif op == "/":
                calculation = value1/value2
        elif op == "+":
            calculation = value1 + value2
        else:
            calculation = value1 - value2

        #If the answer has no decimals it will come out as an integer
        if calculation == int(calculation):
             calculation = int(calculation)

        #Rounds it so there aren't too many decimal places
        else:
             calculation = round(calculation,5)

        #Prints answer
        print(f"The answer is {calculation}")

        #Writes the working out into a file
        file = open('Working.txt','a')
        file.write(f"{value1} {op} {value2} = {calculation}\n")

    #If they enter a non-number or enter 0 for division, an exception will occur
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
         print("you cannot divide by 0, enter a different value.")
    except Exception:
         print("Invalid input. Please enter either x / + or - ")
         
    finally:
         if file is not None:
            file.close

