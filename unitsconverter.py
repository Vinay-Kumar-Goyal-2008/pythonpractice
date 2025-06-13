import time

def kgtog():
    try:
        kg=int(input('Enter the vaue of kgs:-'))
    except Exception as e:
        print(e)
        kgtog()
    else:
        print(f"The value of g for the given kg is {kg*1000}g")
def kmtom():
    try:
        km=int(input('Enter the vaue of kms:-'))
    except Exception as e:
        print(e)
        kmtom()
    else:
        print(f"The value of m for the given km is {km*1000}m")
def mtocms():
    try:
        m=int(input('Enter the vaue of m:-'))
    except Exception as e:
        print(e)
        mtocms()
    else:
        print(f"The value of cm for the given m is {m*1000}cm")
def gtopounds():
    try:
        g=int(input('Enter the vaue of g:-'))
    except Exception as e:
        print(e)
        gtopounds()
    else:
        print(f"The value of pounds for the given kg is {g*0.0022}pounds")
def stoms():
    try:
        s=int(input('Enter the vaue of s:-'))
    except Exception as e:
        print(e)
        stoms()
    else:
        print(f"The value of ms sfor the given s is {s*1000}ms")
def exit():
    print("Thabk You for using this program")




def main():
    print('''
    Welcomr to tkhe unit converter program here you can convert the desired unit into the units you want:-''')
    time.sleep(2)
    print('''
    Enter the unit conversion you want to do:-
        
        1. kg to g
        2. km to m
        3. g to pounds
        4. m to cms
        5. s to ms
        6. Exit
    ''')
    try:
        ch= int (input("Enter your choice:-  "))
    except Exception as e:
        print (e)
        main()
    else:
        match ch:
            case 1:
                kgtog()
                main()
            case 2:
                kmtom()
                main()
            case 3:
                gtopounds()
                main()
            case 4:
                mtocms()
                main()
            case 5:
                stoms()
                main()
            case 6:
                exit()
            case _:
                print('Please enter a valid choice')
                main()
main()