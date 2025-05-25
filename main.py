import random
while True:
    n= int(1+random.random()*999)
    no=0
    while True:
        num= int(input('Enter the guess number:-  '))
        if (num>n) :
            print('Your number is greater than the given number')
        elif (num<n) :
            print('Your number is less than the given number')
        else:
           print('Congratulations! You have guessed the original number')
           print("Number of guesses:- ",no+1)
           if ((no+1)<10):
                print("Congratulations! You have won the game")
           else:
                print("You have lost the game! Better luck next time")
           break
        no+=1
    ch= input('do you want to continue playing game (y/n)')
    if (ch=='n'):
        break