import pandas as pd
import time as t
data=pd.read_csv('netflix_titles.csv')
def scr1():
    print('Welcome to the netflix dataset analysis program!')
    t.sleep(2)
    scr2()
def scr2():
    print('What do you want to do?')
    print('''
1. Load refined data
2. Find the number of movies and shows in netflix and compare them
3. Find the oldest realase year and the movie/show released in that year
4. List the number of movies released in a particular year
5. Filter the dataset with country and display the data of a particular country
6. Exit ''')
    try:
        ch=int(input('ENter your choice:-  '))
        if ch==1:
            print(display())
        elif ch==2:
            print(no_of_movies())
        elif ch==3:
            print(oldest())
        elif ch==4:
            year=int(input('Enter the year:-  '))
            print(no_movies(year))
        elif ch==5:
            country=input('Enter the country:-  ')
            print(datacountry(country))
        elif ch==6:
            exit(1)
        else:
            print('Invalid Input')
            scr1()
        scr1()
    except Exception as e:
        print(e)
        scr2()
def display():
    return data
def no_of_movies():
    df=data.groupby('type')['type']
    movies=df.get_group('Movie').count()
    tv=df.get_group('TV Show').count()
    print(f'{'movies' if movies>tv else 'TV Shows'} are more than the other on netflix.')
    return pd.DataFrame({
        'movie':movies,
        'tv show':tv
    }, index=['Number'])
def oldest():
    data['date_added'] = pd.to_datetime(data['date_added'], format='mixed')
    df=data[data.date_added==data['date_added'].min()]
    return df.loc[:,['type','release_year','date_added','title','director','rating']]
def no_movies(year):
    print(data[data.release_year==year])
    return f'Total no of movies or shows released in {year} are {data[data.release_year==year]['release_year'].count()}'
def datacountry(country):
    country=country.strip().title()
    print(data.groupby('country').get_group(country))
    return f'Total no of movies or shows of {country} are {data.groupby('country').get_group(country)['country'].count()}'
scr1()