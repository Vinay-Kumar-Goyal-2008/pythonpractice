import requests
import random
res=requests.get('https://opentdb.com/api.php?amount=20&category=9&difficulty=medium&type=multiple')
ques=res.json()['results']
score=0
for i in ques:
    print(i['question'])
    options=[i['correct_answer']]+i['incorrect_answers']
    random.shuffle(options)
    c=1
    d={}
    for j in options:
        d[c]=j
        print(c,j)
        c+=1
    ch=int(input('Enter your choice:-'))
    if d[ch]==i['correct_answer']:
        print('Correct answer')
        score+=1
    else:
        print('Incorrect answer')
    print()
    print()
    print()
print(f'Your scote is {score}')