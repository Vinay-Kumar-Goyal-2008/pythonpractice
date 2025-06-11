import time
def display():
    with open('todolist.txt','r') as f:
        data=f.readlines()
        for i in data:
            print(i,end='')
def add():
    with open('todolist.txt','a') as f:
        data=input('Enter the name of the task you want to add:-')
        f.write(f'{data}-----Not Done\n')
        print(f'Congratulations!Your Data has been successfully added to the todolist.\n')
def markdone():
    with open('todolist.txt','r') as f:
        taskname=input('Enter the task you want to mark as done:-')
        data= f.readlines()
    with open('todolist.txt','w') as f:
        for i in data:
            newdata= i.split('-----')
            if newdata[0]==taskname:
                newdata[1]='Done'
            wholedata='-----'.join(newdata)
            f.write(wholedata+'\n')
        print('Your Task has been mark done.')
def edit():
    with open('todolist.txt','r') as f:
        taskname=input('Enter the task you want to edit:-')
        newtaskname=input('Enter the new task name you want to change:-')
        data= f.readlines()
    with open('todolist.txt','w') as f:
        for i in data:
            newdata= i.split('-----')
            if newdata[0]==taskname:
                newdata[0]=newtaskname
            wholedata='-----'.join(newdata)
            f.write(wholedata+'\n')
        print('Your Task has been edited.')
def delete():
    with open('todolist.txt','r') as f:
        taskname=input('Enter the task you want to delete:-')
        data= f.readlines()
    with open('todolist.txt','w') as f:
        for i in data:
            newdata= i.split('-----')
            if newdata[0]==taskname:
                continue
            else:
                wholedata='-----'.join(newdata)
                f.write(wholedata+'\n')
        print('Your Task has been delete.')
def exit():
    print('You have exitted the progeam')
def main():
    time.sleep(2)
    print('*'*140)
    print('*'*140)
    print(' '*60,"Todo List")
    print('*'*140)
    print('*'*140)
    time.sleep(2)
    print('''
    Choices:-
    1. Display the list
    2. Add new task to the list
    3. Mark a task on the todo list as done
    4. Edit Existing Tasks
    5. Delete Existing Task
    6. Exit
    ''')
    try:
        ch=int(input('Enter Your Choicea:-'))
        if ch==1:
            display()
            main()
        elif ch==2:
            add()
            main()
        elif ch==3:
            markdone()
            main()
        elif ch==4:
            edit()
            main()
        elif ch==5:
            delete()
            main()
        elif ch==6:
            exit()
        else:
            print('Invalid Choice! Please Try Again')
            main()
    except Exception as e:
        print(e)
        main()
main()