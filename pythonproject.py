import random
wires = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
bomb = random.sample(wires, 2)
safe = random.sample(wires, 2)

def defuse():
    print("The bomb wil explode unless the correct wire is cut.")
    print
    print("The wires are numbered 1, 2, 3, 4, and 5")
    cutter = raw_input("Which wire?: ")
    chances = 4
    
    while cutter != safe:
        chances = chances - 1
        cutter = raw_input("Which wire?: ")