health = (25)#globle variables lollolololo
strength = int(10)
strength_potion = strength + int(5)
medkit = health + int(10)
bug_health = int(20)
bug_attack = int(5)
code_essence = (100)
null_health = 50
null_attack = 15
def start_adventure():#something meta game
    print("Placeholder because i cant think of anything")
    print("1. Stay at your home") #think of something idiot
    print("2. Enter Visual Studio Swamp")
    choice = input(">")

    if choice == "1":
        Home()
    elif choice == "2":
        VSswamp()
    else:
        print("Invalid input")
        start_adventure()#figure out how to actually call the funcions idiot

def VSswamp():
    print("You come to a split in your path")
    print("1. Head left")
    print("2. Head right")
    choice = input(">")#might have to change choice
    #nvm
    if choice == "1":
        left()
    elif choice == "2":
        right()
    else:
        print("Invalid input")
        VSswamp()
def Home():# i got lazy
    print("You decide to stay at home, not knowing youre slowly becomming corrupted. When you finally notice it, it is to late. CORRUPTED")
   
   

def left():
    print("A bug attacks!")
    print("Your health: " + str(health))
    print("Your attack: " + str(strength))
    print("1. Bash")
    print("2. Run")
    choice = input(">")

    if choice == "1":
        bashmove()
    elif choice == "2":
        run()
    else:
        print("Invalid Input")
        left()

def bashmove():
    print("Dealed " + str(strength) + " damage to bug!")
    bash = bug_health - strength
    print("Bug HP: " + str(bash))
    if bug_health <= (0):#how on earth do i do this
        print("Bug became tame!")
        object_encounter()
    elif bug_health >= (0):
        print("Bug Dealt 5 damage!")
        attack = health - bug_attack
        if attack <=0:
            print("You collapsed!")
        else:
            print("HP: " + str(attack))
            print("1. Bash")
            print("2. Run")
            choice = input(">")
            if choice == "1":
                bashmove()#my god please kill me
            elif choice == "2":
                 run()
            else:
                print("invalid imput")
                

        


def run():
    import random
    random_boolean = random.choice([True, False])
    if random_boolean == True:
        print("Succsessfully ran away!")
        object_encounter()
    else:
        print("You tried to get away, but failed!")
        left()



def right():
    print("You come to a corrupted river")
    print("1. Turn around")
    print("2. Wade through it")
    choice = input(">")
    if choice == "1":
        VSswamp()

    elif choice == "2":#lazy again
       river_crossing()
    else:
        print("Invalid input")
def object_encounter():
    print("you see a strange object on the side of the path")
    print("1. pick it up")
    print("2. Continue to GIThub grove")
    choice = input(">")
    
    if choice == "1":
        s_object()
    elif choice == "2":
        github_grove()
    else:
        print("Invalid input")


def river_crossing():
    import random
    random_boolean = random.choice([True, False])
    if random_boolean == True:
        print("You successfully crossed the river as you continue on your path")
        object_encounter()
    else:
        print("You try to wade through but you realize that it is far to deep. you become corrupted")
def s_object():
    print("As you aproach the object, you feel a strange force emminating from it")
    import random
    random_boolean = random.choice([True, False])
    if random_boolean == True:
       print("You find the object is a mythical CODE ESSENCE")
       print("You pocket the item for later")
       github_grove()
       return code_essence == True
       
    else:#lazy #2
        print("When you grab the object, you suddenly feel a force going through you, as the object is slowly corrupting you.")
        



def github_grove():
    print("you enter a small town called github grove")
    print("1. Stay at the motel")
    print("2. continue to NULL")
    print("3. Talk to the guide")
    choice = input(">")
    if choice == "1":
        motel()
    elif choice == "2":
        NULLBOSSAPROACH()
    elif choice =="3":
        guide()
    else:
        print("Invalid input")
        github_grove()
    #how
def motel():#got lazy again
    print("You deside to say at the motel, however you quickly realize that this motel is corrupted. before you can escape you also become corrupted. END")

def guide():
    print("Hello there young traveler! You must be searching for NULL right? Well i can tell you his palace is to the left of the Terminal. Also i belive i have a few things that could help you on your adventure. Good luck out there!")
    print("The man gave you a medkit and a strength potion")
    print("HP: " + str(medkit))
    print("Attack: " + str(strength_potion))
    NULLBOSSAPROACH()

def NULLBOSSAPROACH():
    print("You find yourself facing the TERMINAL Temple, inside lives the NULL")
    print("1. Fight the boss")
    print("2. Turn around")
    choice = input(">")
    if choice == "1":
        NULLBOSS()
    elif choice == "2":
        Turn()
    else:
        print("Invalid input")
        NULLBOSSAPROACH()






def NULLBOSS():
    print("As you enter the temple, you see NULL; a mass of corrupted code")
    print("NULL attacks!")
    print("NULL hp: 50")
    print("1. Bash")
    print("2. Defend")
    print("3. View items")
    print("4. Run")
    choice = input(">")

    if choice == "1":
        nullbash()
    elif choice == "2":
        defend()    
    elif choice == "3":
        codeessence_null()
    elif choice == "4":
        nullrun()
    else:
        print("Invalid Input")
        NULLBOSS()
def codeessence_null():
    
    if code_essence == True:
        print("You use CODE ESSENCE against NULL")
        print("Delt " + str(code_essence) + "Damage to NULL")
        print("NULL collapsed!")
    else:#work damnit
        print("You find your bag empty")
        NULLBOSS() 
    return code_essence
    
    

def nullbash():
    print("Delt placeholder damage to NULL!")
    if null_health <= (0):
        end()
        
    elif null_health >= (0):
        print("NULL Dealt 15 damage!")
        attack = health - null_attack
        if attack <=0:
            print("You collapsed!")
        else:
             print("HP: " + str(attack))
             print("1. Bash")
             print("2. Run")
             choice = input(">")
             if choice == "1":
               nullbash()
             elif choice == "2":
                nullrun()

def defend():
    print("Used defence!")
    print("You now block 40 percent of incoming damage!")



def nullrun():#lazy #3
    print("As you try to run away, you find that the exit has been block.")
    print("There is nothing you can do before NULL grabs you and corrupts you")


def Turn():#lazy #4
    print("You decide to turn around and stay at Github Grove")
    print("When you wake up next morning you hear rumbling, as you look to the Terminal Temple, you see a giant mass of corrupted code")
    print("There is nothing you  can do before the mass corrupts the entire city")







def end():
    print("You sucsessfully defeated NULL! THE END")






































start_adventure()




