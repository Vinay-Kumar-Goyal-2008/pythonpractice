import os
directory= input('Enter the directory path:-    ')
forma= input('Enter the format of file you do not want to format:-     ')
f= open('harry.txt')
data= f.read()
newdata= data.split('\n')
os.chdir(directory)
directories= os.listdir(directory)
files=[]
for i in directories:
    if os.path.isfile(i):
        files.append(i)
for i in files:
    for j in newdata:
        if (i.startswith(j) or i.endswith(forma) or i=="harry.txt"):
            continue
        else:
            os.rename(i,i.capitalize())