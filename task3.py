name= input("Please enter the participants name: ")
swimming = int(input("Enter swimming time: "))
cycling = int(input("Enter cycling time: "))
running = int(input("Enter running time: "))
triathalon_time = swimming + cycling + running
qualifying_time = 100
if triathalon_time <= qualifying_time:
    print(f"Congratulations {name}, you've received Provincial Colours!")
elif triathalon_time <= qualifying_time+5:
    print(f"Congratulations {name}, you've received Provincial Half Colours!")
elif triathalon_time <= qualifying_time+10:
    print(f"Congratulations {name}, you've received a Provincial Scroll!")
else:
    print(f"Sorry {name}, you haven't achieved an award this time")