import numpy as np
print('''
Welcome to movie rating software:-
There are a total of 20 movies from movie 0 to movie 19 rated by 100 people.
''')
rating=np.random.randint(11,size=2000).reshape(20,100)
while True:
    print('''
    What do you want to do:-
        1. find average rating of a movie
        2. find sum of all the ratings of a movie
        3. find min rating of a movie
        4.find max rating of a movie
        5. find median rating of a movie
        6. find the rating done by a particular person
        7. Exit''')
    try:
        ch=int(input('Enter your choice:-'))
        if (ch==1):
            mov=int(input('Enter the number of movie:-'))
            print(np.mean(rating[mov]))
        elif (ch==2):
            mov=int(input('Enter the number of movie:-'))
            print(np.sum(rating[mov]))
        elif (ch==3):
            mov=int(input('Enter the number of movie:-'))
            print(np.min(rating[mov]))
        elif (ch==4):
            mov=int(input('Enter the number of movie:-'))
            print(np.max(rating[mov]))
        elif (ch==5):
            mov=int(input('Enter the number of movie:-'))
            print(np.median(rating[mov]))
        elif (ch==6):
            mov=int(input('Enter the number of movie:-'))
            cust=int(input('enter user number scaling from 0 to 99:- '))
            print(rating[mov,cust])
        elif (ch==7):
            break
    except Exception as e:
        print(e)