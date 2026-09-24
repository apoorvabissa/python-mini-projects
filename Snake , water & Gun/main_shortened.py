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

if(computer==you):
    print("Tie")
else:
    '''
    if(computer==-1 and you==0): computer-you=-1
    print("You Loose!")

elif(computer==1 and you==0): computer-you=1
    print("You Win!")

elif(computer==0 and you==1): computer-you=-1
    print("You Loose!")

elif(computer==0 and you==-1): computer-you=1
    print("You Win!")

elif(computer==1 and you==-1): computer-you=2
    print("You Loose!")

elif(computer==-1 and you==1): computer-you=-2
    print("You win!")
        '''
    if((computer-you)==-1 or (computer-you)==2):
        print("You Lose!")
    else:
        print("You win!")