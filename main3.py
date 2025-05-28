import random
def exit():
    print('Thank You for playing the game! Come again next time.')
def main():
    print('*'*120)
    print('*'*120)
    print(' '*40,'Welcome to SNAKE, WATER GUN GAME')
    print('*'*120)
    print('*'*120)
    print('''Instructtions:-
          1.This game will be played with the computer
          2. You would have to choose and write your choice (s,w,g)
          3. This game will be played for 10 rounds
          4. Out of 10 rounds who win the maximum rounds will be declared as winner
          5. Good Luck''')
    game=['s','w','g']
    comp=0
    user=0
    for i in range(10):
        comp_choice= random.choice(game)
        user_choice= input('Enter Your Choice (s,w,g):-  ')
        if user_choice not in 'swg':
            print('INVALID INPUT')
            print('PLEASE TRY AGAIN!')
            main()
        winner=['sw','wg','gs']
        result_comp=comp_choice+user_choice
        result_user=user_choice+comp_choice
        if result_comp in winner:
            print('COMPUTER WON THE ROUND')
            comp+=1
        elif result_user in winner:
            print("CONGRATULATIONS! YOU WON THE ROUND")
            user+=1
        else:
            print('ITS A DRAW')
    print(f"user-{user}")
    print(f"computer- {comp}")
    if (user>comp):
        print("CONGRATULATIONS YOU WON THE GAME")
    elif (user<comp):
        print("COMPUTER WON THE GAME! BETTER LUCK NEXT TIME")
    else:
        print('THIS GAME IS A DRAW')
    choice= input('Do you want to continue playing the next game (y/n):-')
    if choice in'yY':
        main()
    else:
        exit()
main()