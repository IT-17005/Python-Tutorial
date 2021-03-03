from random import randint

for x in range(1,6):
    num = int(input("Enter any number between 1-5: "))
    randNum = randint(1,5)
    if num == randNum:
        print("I've Won the Game.")
    else:
        print("I've lose the Game.")

    print("The random number was:",randNum)
