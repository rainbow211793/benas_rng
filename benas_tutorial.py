import time
import random
import variables

print("Here you can roll and get badges. Try and get every badge and get some very rare rolls.")
time.sleep(0.3)
input("->")
print("The possibilities are endless with the 1 billion available numbers that can be rolled.")
time.sleep(0.5)
input("->")
print(" ")

print("Here are some mechanics to show you how to game functions")
rng = random.randint(1,1000000000)
time.sleep(0.3)
input("->")
print(rng)
print("You see this? You rolled once")
input("->")
print(" ")
time.sleep(1)

print("Next up are badges, every roll you do will contribute to a statistic that can you can possibly earn badges on.")
time.sleep(0.3)
input("->")
print("Since you technically rolled once, here is one free badge for you!")
time.sleep(0.5)
input("->")

if 0 < rng :
    badges = 1
    print("You have earned the badge \"First Roll\"")
    print(" ")
    
print("Well done! You have officially finished the tutorial. You can rerun this again if needed.")
time.sleep(0.3)
input("->")

import benas_game