import random
import time
import csv

# ────────────────────

# Tutorial
print("「 ✦ Benas RNG ✦ 」")
print("Hello and welcome to Benas RNG")
print("press enter when you see a -> or do ! to skip the tutorial")
time.sleep(0.3)
ans = input("->")
if ans == "!" :
    import benas_game
else :
    import benas_tutorial