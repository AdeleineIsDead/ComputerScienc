import random 


user_input = ""
while user_input != str(number):
    number = random.radiant[1, 100]
    user_input = int(input("Guess\n>"))
    if user_input > number:
        print("Too high")
    elif user_input < number:
        print("Too low")
    elif user_input == number:
        print("correct")