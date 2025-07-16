import pandas as pd
import time as t
df=pd.read_csv('Reviews.csv')
df=df[['Id','ProductId','UserId','ProfileName','Score','Time']]
while True:
    print('*'*70)
    print('Welcome to Amazon Review Analyser Program')
    print('*'*70)
    t.sleep(2)
    print('What do you want to do:-')
    print('''
          1. Show total number of reviews
          2. Show average rating
          3. Show number of reviews per rating (1-5)
          4. Show top 10 most reviewed products
          5. SHow top 10 highest-rated products
          6. Show product with most 1-star reviews
          7. Show top 10 reviewers by review count
          8. Show average rating given by each reviewer (top 10)
          9. Exit ''')
    t.sleep(2)
    try:
        ch=int(input('Enter your choice:-   '))
        if ch==1:
            print(f"There are currently {df['Id'].count()} reviews available in our database for amazon review analysis")
            t.sleep(2)
        elif ch==2:
            print(f'The average rating of all the products currently available given by different users is :- \n {df.Score.mean()}')
        elif ch==3:
            ans= pd.Series([df[df.Score==i].Id.count() for i in range (1,6)], index=[f'{i} rating' for i in range(1,6)])
            print(ans)
        elif ch==4:
            ans= df.groupby('ProductId', group_keys=True)
            maxcount=ans.ProductId.count().sort_values(ascending=False)[0:10]
            print(maxcount)
        elif ch==5:
            ans= df.groupby('ProductId')
            a=ans.Score.mean().sort_values(ascending=False)[0:11]
            print(a)
        elif ch==6:
            ans= df[df.Score==1].groupby('ProductId')
            a=ans.ProductId.count().sort_values(ascending=False)[0:1]
            print(f'The product having most 1 rating is the product with product id {a.index[0]} with {a.iloc[0]} rating 1 reviews.')
        elif ch==7:
            ans= df.groupby(['UserId','ProfileName'])
            a= ans['ProfileName'].count().sort_values(ascending=False)[0:10]
            print(a)
        elif ch==8:
            ans= df.groupby(['UserId','ProfileName'])
            a= ans.Score.mean().sort_values(ascending=False)[0:10]
            print(a)
        elif ch==9:
            break
        else:
            print('THe choice you have entered is incorrect! Please try again.')
            continue
    except Exception as e:
        print(e)
        t.sleep(2)
        continue
exit(0)