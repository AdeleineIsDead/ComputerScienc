#nested if statements
#you are a primememer
prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >=18:
        print("You are elegable for free shipping")
    else:
        if consent:
            print("You are elegable for free shipping")
        else:
            print("shut up")

elif cost >= 25:
    if age >= 18:
        print("You are elegable for free shipping")
    elif consent:
        print("You are elegable for free shipping")
    else: 
        print("shut up")

else: 
    print("shut up")


