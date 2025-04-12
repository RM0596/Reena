import random
target=random.randint(1,50)
while True:
    Userchoice = input("Guess the target or Quit(Q) :")
    if(Userchoice == "Q"):
        break
    Userchoice=int(Userchoice)
    if (Userchoice == target):
        print("suceess: Correct guess...")
        break
    elif (Userchoice < target):
        print("Your number was small. Take a bigger guess....")
    else:
        print("Your number was big. Take a small guess....")
        
print("Game Over....")
    