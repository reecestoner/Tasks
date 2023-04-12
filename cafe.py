#Setting the items in the various lists and dictionsaries
menu = ["Sausage","Eggs","Bacon","Tea"]
stock ={"Sausage" : 40,
        "Eggs" : 48,
        "Bacon" : 30,
        "Tea" : 80 }
price = {"Sausage" : 2,
         "Eggs" : 1,
         "Bacon" : 1.50,
         "Tea": 1}

#Setting price as 0 to be able tp iterate
total_price = 0
#For each item in the menu, the price is multiplied by the stock and added to the total price
for item in menu:
    total_price += stock[item]*price[item]

print(f"The total price of the stock is £{total_price}")