import math
name = input("Please enter your name:\n")
print(f"""Hi {name}, Please choose from one of the following options:\n
Investment - To calculate the  amount of interest you'll earn on your investment\n
Bond - To calculate the amount you'll have to pay on a home loan\n""") # Clear instructions with spacing so its not overwhelming
selection = input("What is your selection?\n").lower() # Any input is converted to lower case so that it causes no errors
if selection == "investment" :
    P = float(input("Enter your deposit amount:\n£"))
    r = (int(input("Enter the interest rate:\n")))/100
    t = int(input("How many years will you be investing?\n"))
    interest = input("Would you like simple or compound interest?\n").lower()
    simple_interest = round((P*(1+r*t)),2) # Formulae
    compound_interest = round((P * math.pow((1+r),t)),2) # Learnt the round function from w3schools.com as money is 2dp
    simple_profit = round((simple_interest -P),2) # Calculates the profits of simple and compound
    compound_profit = round((compound_interest -P),2) 
    if interest == "simple":
        print(f"Your investment will return £{simple_interest} after {t} years; a total of £{simple_profit} profit.")
    elif interest == "compound":
        print(f"Your investment will return £{compound_interest} after {t} years; a total of £{compound_profit} profit.")
    else:
        print("Invalid input. Please type simple or compound")
if selection == "bond":
    P = float(input("Enter the prevent value of the house:\n"))
    i = (int(input("Enter the interest rate:\n")))/(100*12) #interest rate converted into decimal and monthly
    n = int(input("How many months do you wish to make repayments?\n"))
    monthly_repayment = round(((i*P)/(1-(1+i)**(-n))),2)  # formulae
    print(f"Your repayment per month will be £{monthly_repayment} for {n} months.")