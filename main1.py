def pattern():
    n= int(input('Enter the number of rows:-'))
    boo= int(input('Enter boolean value:-  '))
    if (boo>1):
        print('Invalid boolean input')
        pattern()
    else:
        boo =bool(boo)
        if (boo==True):
            for i in range(1,n+1):
                for j in range(1,i+1):
                    print('*',end=' ')
                print()
        else:
            for i in range(n,0,-1):
                for j in range(1,i+1):
                    print('*',end=' ')
                print()
pattern()