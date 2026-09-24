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

if(computer==-1 and you==0):
    print("You Loose!")

elif(computer==0 and you==0):
    print("Tie!")

elif(computer==1 and you==0):
    print("You Win!")

elif(computer==-1 and you==1):
    print("You Win!")

elif(computer==0 and you==1):
    print("You Loose!")

elif(computer==1 and you==1):
    print("Tie!")

elif(computer==-1 and you==-1):
    print("Tie!")

elif(computer==0 and you==-1):
    print("You Win!")

elif(computer==1 and you==-1):
    print("You Loose!")

else:
    print("Something went wrong")


