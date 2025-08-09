# TradingBot Greeting Script
# Created as part of my early Python learning journey

print("Hello, I'm a TradingBot!")

name = input("What is your name?").strip().title()
if not name:
    name = "Guest" 

print(f"Hello, {name}!")

age = input("What is your age?").strip()

if not age:
    print("Please enter a valid dage.")
else:
    if age.isdigit(): 
        age = int(age)
        if age == 18:
            print("Welcome to the TradingBot!")
        elif age > 18:
            print("You are old enough to use this TradingBot!")
        else:
            print("You must be 18 or older to use this TradingBot.")
    else:
        print("Age must be a number.")

