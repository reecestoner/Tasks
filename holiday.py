#try:
city_flight = input("Please type in your destination (Rome, Milan, Paris or New York):\n").lower
 #   while city_breaks != "rome" and "milan" and "paris" and "new york":
  #      city_breaks = input("Please type one of the following cities: Rome, Milan, Paris or New York:\n")
    
num_nights = int(input("Please enter the number of nights you would like to stay:\n"))
   # while num_nights < 1:
    #    num_nights = int(input("Please enter at least 1 night.\n"))

rental_days = int(input("How many days of car rental would you like?:\n"))
    #while rental_days < 0:
     #   rental_days = int(input(("Please enter at least 0 days.\n")))
    #print(city_breaks)
    #print(num_nights)
    #print(rental_days)
#except ValueError:
 #   print("Please enter the number of nights as a whole number")

def hotel_cost(x,y=45):
    x = num_nights
    total_hotel = x * y
    return total_hotel
print(hotel_cost(num_nights))

def  plane_cost(x):
    if x == "rome":
        y = 80
    elif x == "milan":
        y = 100
    elif x == "paris":
        y = 50
    else:
        y = 600
    flight_cost = y
    return flight_cost
print(plane_cost(city_flight))
def car_rental(y, x = 30):
    y = rental_days
    car_cost = x * y
    return car_cost
print(car_rental(x,y))
def holiday_cost( x, y, z  ):
    x = hotel_cost()
    y = plane_cost()
    z = car_rental()
    total = x + y + z
    print(total)


print(holiday_cost())
