import pandas as pd

data=pd.read_csv('C:\\Users\\Vinay Kumar Goyal\\OneDrive\\Desktop\\owid-covid-data.csv')
def groupallcountries():
      newdata={}
      countries={}
      allcountries=dict(data.loc[:,'location'])
      for i in allcountries:
            if (allcountries[i] not in countries.values()):
                  countries[i]=allcountries[i]
      countries=dict(countries)
      n=0
      for i in countries:
            totalcases=data.groupby('location')['new_cases'].sum()[countries[i]]
            totaldeaths=data.groupby('location')['new_deaths'].sum()[countries[i]]
            newdata[n]=[data.loc[i,'iso_code'],data.loc[i,'continent'],countries[i],totalcases,totaldeaths, data.loc[i,'population']]
            n+=1
      newdata=pd.DataFrame(dict(newdata), index=['iso_code','Continent','Country','Total Cases','Total Deaths','Total Population'])
      newdata=newdata.T
      return newdata
print('''
Welcome to covid management which can analyse the data and display data in acccordamce to your priference:-

      What do you want to do:-
      1.  display the whole table
      2.  display top 10 countries by total cases
      3.  display top 10 countries by total deaths
      4.  display top 10 countries by highest death rate
      5.  display the total number of cases world wide
      6.  display the total number of cases in a particular country
      7.  display the day with most number of deaths worldwide
      8.  compare two countries in terms of total death and total cases and predict the mmost safest country amoung the two
      9.  display the most safest country worldwide
      10. Show the detailed analysis of a particular country
      11. Display raw table
''')
ch=int(input('Enter your choice:-  '))
if ch==1:
      newdata=groupallcountries()
      print(newdata)
elif ch==2:
      newdata=groupallcountries()
      newdata=newdata.sort_values(by='Total Cases', ascending=False).reset_index(drop=True)
      for i in range(10):
            print(newdata.loc[i,'Country'] ,'       -        ',newdata.loc[i,'Total Cases'])
elif ch==3:
      newdata=groupallcountries()
      newdata=newdata.sort_values(by='Total Deaths', ascending=False).reset_index(drop=True)
      for i in range(10):
            print(newdata.loc[i,'Country'] ,'       -        ',newdata.loc[i,'Total Deaths'])
elif ch==4:
      newdata=groupallcountries()
      newdata['Death Rate']=[
      (newdata.loc[i, 'Total Deaths'] / newdata.loc[i, 'Total Cases'] * 100) 
      if newdata.loc[i, 'Total Cases'] and pd.notna(newdata.loc[i, 'Total Cases']) 
      else 0 
      for i in newdata.index
      ]
      newdata=newdata.sort_values(by='Death Rate', ascending=False).reset_index(drop=True)
      for i in range(10):
            print(newdata.loc[i,'Country'] ,'       -        ',newdata.loc[i,'Death Rate'])
elif ch==5:
      newdata=groupallcountries()
      for i in newdata.index:
            if newdata.loc[i,'Country']=='World':
                  print(newdata.loc[i,'Total Cases'])
elif ch==6:
      newdata=groupallcountries()
      country=input('Enter The country you want to check total number of cases:-  ')
      for i in newdata.index:
            if newdata.loc[i,'Country']==country:
                  print(newdata.loc[i,'Total Cases'])
elif ch==7:
      newdata=groupallcountries()
      for i in newdata.index:
            if newdata.loc[i,'Country']=='World':
                  print(newdata.loc[i,'Total Deaths'])
elif ch==8:
      newdata=groupallcountries()
      c1= input('Enter name of first country:-   ')
      c2=input('Enter name of second country:-   ')
      print ()
      print(c1)
      for i in newdata.index:
            if newdata.loc[i,'Country']==c1:
                  totalcasesc1=newdata.loc[i,'Total Cases']
                  totaldeathsc1=newdata.loc[i,'Total Cases']
                  populationc1=newdata.loc[i,'Total Population']
                  print(f'''
Total Cases:-  {totalcasesc1}
Total Deaths:-  {totaldeathsc1}
Chances to get infected:-  {(totalcasesc1/populationc1)*100}''')
      print()
      print(c2)
      for i in newdata.index:
            if newdata.loc[i,'Country']==c2:
                  totalcasesc2=newdata.loc[i,'Total Cases']
                  totaldeathsc2=newdata.loc[i,'Total Cases']
                  populationc2=newdata.loc[i,'Total Population']
                  print(f'''
Total Cases:-  {totalcasesc2}
Total Deaths:-  {totaldeathsc2}
Chances to get infected:-  {(totalcasesc2/populationc2)*100}''')
      if ((totalcasesc2/populationc2)*100>(totalcasesc1/populationc1)*100):
            print(f"{c1} is safer than {c2}")
      else:
            print(f"{c2} is safer than {c1}")
elif ch==9:
      newdata=groupallcountries()
      r=[]
      for i in newdata.index:
            if newdata.loc[i,'Country']=='World':
                  continue
            else:
                  r.append(((newdata.loc[i,'Total Cases']/newdata.loc[i,'Total Population'])*100))
      name=newdata.loc[r.index(min(r)),'Country']
      print(f'{name} is the safest place to live in the world')
elif ch==10:
      newdata=groupallcountries()
      c=input('Enter the name of the country:-   ')
      for i in newdata.index:
            if newdata.loc[i,'Country']==c:
                  print(newdata.loc[i])
                  print('Chances to get infected:-  ', ((newdata.loc[i,'Total Cases']/newdata.loc[i,'Total Population'])*100))
                  print('Death Rate:-  ', (newdata.loc[i, 'Total Deaths'] / newdata.loc[i, 'Total Cases'] * 100) )
elif ch==11:
      print(data)