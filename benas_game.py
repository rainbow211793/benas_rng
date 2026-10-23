import variables
import random

# is_between_int function

def is_between_int(num, low, high):
    return num in range(low, high + 1)

# Example
# print(is_between_int(10, 20, 25)) - Returns "True"
# print(is_between_int(25, 10, 25)) - Return "False"

while variables.loop < 5 :
    print("「 ✦ Benas RNG ✦ 」")
    print("1. Roll\n2. Stats\n3. Badges\n?.?!?!?!\n5. Quit")
    ans = input("Choose what you would like do next")
    
    if ans == "1." or ans == "Roll" or ans == "1" or ans == "1. Roll" or ans == "1. roll" or ans == "roll" :
        variables.rng = random.randint(1,1000000000)
        print(" ")
        print(variables.rng)
        variables.rolls = variables.rolls + 1
        print(" ")
        if is_between_int(variables.rng, 1,100000000) :
            print("You have earned the badge \"1 in 10\" ")
            print(" ")
            if variables.b2 == False :
                variables.badges = variables.badges + 1
                variables.b2 = True
        if is_between_int(variables.rng, 1,10000000) :
            print("You have earned the badge \"1 in 100\" ")
            print(" ")
            if variables.b3 == False :
                variables.badges = variables.badges + 1
                variables.b3 = True
        variables.save()
    elif ans == "2." or ans == "Stats" or ans == "2" or ans == "2. Stats" or ans == "2. stats" or ans == "stats" :
        print(" ")
        print("Your statistics!")
        print(f"Plays = {variables.plays}\nRolls = {variables.rolls}\nBadges = {variables.badges}")
        print(" ")
    elif ans == "3." or ans == "Badges" or ans == "3" or ans == "3. Badges" or ans == "3. badges" or ans == "badges" :
        print(" ")
        print("All Badge(s)")
        print("")
        print(" \"First Roll\" ")
        if variables.b2 == True :
            print(" \"1 in 10\" ")
        if variables.b3 == True :
            print(" \"1 in 100\" ")
        print(" ")
    elif ans == "5." or ans == "Quit" or ans == "5" or ans == "5. Quit" or ans == "5. quit" or ans == "quit" :
        variables.loop = 67