import random

computer = random.choice([-1,0,1])

youstr = input("Enter your choice: ")

youDict = {
    "Snake" : -1,
    "Water" : 0,
    "Gun" : 1
}

reverseDict = {
    1:"Snake",
    -1:"Water",
    0:"Gun"
}

you = youDict[youstr]

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")
