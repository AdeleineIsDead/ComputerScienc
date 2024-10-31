
def devide_two():
    try:
        x = int(input("What is the first number\n> "))
        y = int(input("What is the second number\n> "))
        print (x / y)

    except ValueError:
        print("Dumbass")
        devide_two()

    except ZeroDivisionError:
        print("Dumbass")
        devide_two()
    finally:
        print("shut up")
devide_two()