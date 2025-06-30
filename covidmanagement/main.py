import pandas as pd

data=pd.read_csv('C:\\Users\\Vinay Kumar Goyal\\OneDrive\\Desktop\\owid-covid-data.csv')
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
newdata=pd.DataFrame(dict(newdata))
print(newdata)