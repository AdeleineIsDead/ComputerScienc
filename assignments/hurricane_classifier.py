windspeed = int(input("What is the wind speed\n>"))

if windspeed < 74:
    print("Tropical Storm")
elif windspeed < 96:
    print("Category 1")
elif windspeed < 111:
    print("Category 2")
elif windspeed < 130:
    print("Category 3")
elif windspeed < 155:
    print("Category 4")
else:
    print("Category 5")