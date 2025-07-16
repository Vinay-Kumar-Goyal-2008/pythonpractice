import pandas as pd
df = pd.read_csv('top10s.csv', encoding='latin1')
def songsofartist(artist):
    return df[df.artist==artist].title
def songsbygenre(genre):
    songs=df[df['top genre']==genre].title
    if songs.empty:
        return 'No song found for the given genre'
    else:
        return songs
def mostpopularsongs(n):
    return df.sort_values(by='pop', ascending=False).reset_index()[['title','pop']][0:n]
def songsofyear(year):
    songs=df[df.year==year][['title','year']]
    if songs.empty:
        return 'No song found for the given genre'
    else:
        return songs
def getsongbytitle(title):
    songs=df[df.title==title]
    if songs.empty:
        return 'No song found for the given genre'
    else:
        return songs
def energeticsongs():
    return df.sort_values(by='nrgy', ascending=False)[['title','nrgy']][0:5]
def compareartists(artist1,artist2):
    artist1df=df[df.artist==artist1]
    artist2df=df[df.artist==artist2]
    print(artist1df['pop'])
    comparisondf= pd.DataFrame({
        artist1:[artist1df.title.count(),artist1df['pop'].mean(),artist1df.bpm.mean(),artist1df.nrgy.mean(),artist1df.dnce.mean(),artist1df.dB.mean(),artist1df.val.mean(),artist1df.acous.mean(),artist1df.spch.mean()],
        artist2:[artist2df.title.count(),artist2df['pop'].mean(),artist2df.bpm.mean(),artist2df.nrgy.mean(),artist2df.dnce.mean(),artist2df.dB.mean(),artist2df.val.mean(),artist2df.acous.mean(),artist2df.spch.mean()]
    }, index=[
    "number of songs",
    "average popularity",
    "average bpm",
    "average energy",
    "average danceability",
    "average loudness",
    "average valence",
    "average acousticness",
    "average speechiness"
    ])
    return comparisondf
def songsbymood(mood):
    if mood==1:
        return df.sort_values(by='val', ascending=False)[['title','artist','top genre','val']][0:10].set_index(x for x in range(1,11))
    elif mood==2:
        return df.sort_values(by='val', ascending=True)[['title','artist','top genre','val']][0:10].set_index(x for x in range(1,11))
    elif mood==3:
        return df.sort_values(by='nrgy', ascending=False)[['title','artist','top genre','nrgy']][0:10].set_index(x for x in range(1,11))
    elif mood==4:
        return df.sort_values(by='nrgy', ascending=True)[['title','artist','top genre','nrgy']][0:10].set_index(x for x in range(1,11))
    elif mood==5:
        df['motivation_score'] = (df['val'] + df['nrgy'] + df['dnce'] - df['acous'])
        return df.sort_values(by='motivation_score', ascending=False)[['title','artist','top genre','motivation_score']][0:10].set_index(x for x in range(1,11))
    elif mood==6:
        df['motivation_score'] = (df['val'] + df['nrgy'] + df['dnce'] - df['acous'])
        return df.sort_values(by='motivation_score', ascending=True)[['title','artist','top genre','motivation_score']][0:10].set_index(x for x in range(1,11))
    else:
        return 'Wrong input! Try again later!!!'
def longestsong():
    newdf= df[['title','artist','top genre','dur']].sort_values(by='dur',ascending=False)[0:1]
    newdf['dur'] = pd.to_timedelta(df['dur'], unit='s')
    return newdf
while True:
    print('Welcome to the spotify songs program!')
    print("======== SPOTIFY ANALYZER ========")
    print("1. Show all songs by an artist")
    print("2. Show songs from a specific genre")
    print("3. Display most popular songs")
    print("4. Show songs from a specific year")
    print("5. View song details by title")
    print("6. Top 5 energetic songs")
    print("7. Compare two artists")
    print("8. Recommend songs by mood")
    print("9. Find longest song")
    print("10. Exit")
    print("==================================")
    try:
        ch=int(input('Enter your choice:-  '))
        if ch==1:
            artist=input('Enter the name of the artist:-  ')
            artist=artist.title()
            print(songsofartist(artist))
        elif ch==2:
            genre=input('Enter the genre of which you want to show the songs:-  ').lower()
            print(songsbygenre(genre))
        elif ch==3:
            n=int(input('How many songs do you want to display:-  '))
            print(mostpopularsongs(n))
        elif ch==4:
            year=int(input('Enter the year:-  '))
            print(songsofyear(year))
        elif ch==5:
            title=input('Enter the title of the song:-  ')
            print(getsongbytitle(title))
        elif ch==6:
            print(energeticsongs())
        elif ch==7:
            artist1=input('Enter name of first artist:-  ')
            artist2=input('Enter name of second artist:-  ')
            print(compareartists(artist1,artist2))
        elif ch==8:
            print('==========================')
            print('1. Happy')
            print('2. Sad')
            print('3. Energetic')
            print('4. Lazy')
            print('5. Depressed')
            print('6. Motivated')
            print('==========================')
            mood=int(input('Enter your mood choice:-  '))
            print(songsbymood(mood))
        elif ch==9:
            print(longestsong())
        elif ch==10:
            exit(0)
        else:
            print('Invalid choice!!!')
    except Exception as e:
        print(e)
        continue
