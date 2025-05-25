def getdate():
    import datetime
    return datetime.datetime.now()
def exit():
    print('Exitted the program')
def main():
    print('*'*180)
    print('*'*180)
    print(' '*60 , 'Welcome to Health Management Software')
    print('*'*180)
    print('*'*180)
    print('''Whose Data you want to access
        1. Harry
        2. Rohan
        3. Mohd
        4.exit''')
    choice1= input('Enter Your Choice:-  ')
    if (not choice1.isdigit()):
        print('INVALID CHOICE')
        main()
    if (choice1=='4'):
        exit()
    else:
        print(''' Which file do you want to access
            1.Foods
            2. Excercise''')
        choice2= input('Enter Your Choice:-  ')
        if (not choice2.isdigit()):
            print('INVALID CHOICE')
            main()
        print(''' What operation do you want to access
            1. Read the recorded data
            2. Write Record in the file''')
        choice3= input('Enter Your choice:-  ')
        if (not choice3.isdigit()):
            print('INVALID CHOICE')
            main()
        netch= choice1+choice2+choice3
        if netch=='111':
            with open('harryfood.txt','r') as f:
                data= f.read()
                print(data)
            main()
        elif netch=='112':
            with open('harryfood.txt','a') as f:
                food= input('What did you eat:-  ')
                data= food+" - "+str(getdate())
                f.write(data)
                print('Data Successfullty Recorded'.upper())
            main()
        elif netch=='121':
            with open('harryex.txt','r') as f:
                data= f.read()
                print(data)
            main()
        elif netch=='122':
            with open('harryex.txt','a') as f:
                food= input('What exercise did you do:-  ')
                data= food+" - "+str(getdate())
                f.write(data)
                print('Data Successfullty Recorded'.upper())
            main()
        elif netch=='211':
            with open('rohanfood.txt','r') as f:
                data= f.read()
                print(data)
            main()
        elif netch=='212':
            with open('rohanfood.txt','a') as f:
                food= input('What did you eat:-  ')
                data= food+" - "+str(getdate())
                f.write(data)
                print('Data Successfullty Recorded'.upper())
            main()
        elif netch=='221':
            with open('rohanex.txt','r') as f:
                data= f.read()
                print(data)
            main()
        elif netch=='222':
            with open('rohanex.txt','a') as f:
                food= input('What exercise did you do:-  ')
                data= food+" - "+str(getdate())
                f.write(data)
                print('Data Successfullty Recorded'.upper())
            main()
        elif netch=='311':
            with open('mohdfood.txt','r') as f:
                data= f.read()
                print(data)
            main()
        elif netch=='312':
            with open('mohdfood.txt','a') as f:
                food= input('What did you eat:-  ')
                data= food+" - "+str(getdate())
                f.write(data)
                print('Data Successfullty Recorded'.upper())
            main()
        elif netch=='321':
            with open('mohdex.txt','r') as f:
                data= f.read()
                print(data)
            main()
        elif netch=='322':
            with open('mohdex.txt','a') as f:
                food= input('What exercise did you do:-  ')
                data= food+" - "+str(getdate())
                f.write(data)
                print('Data Successfullty Recorded'.upper())
            main()
        else:
            print('INVALID CHOICES! PLEASE TRY AGAIN')
            main()
main()