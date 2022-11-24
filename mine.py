import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


j = 0
df = pd.read_csv('charts.csv')
for index, row in df.iterrows():
    if j < 100:
        #print(row['song'], row['artist'])
        songname = row['song']
        artist = row['artist']
        print(songname)
        print(artist)
        results = spotify.search(songname + " " + artist,type='track')

        items = results['tracks']['items']
        searchterm = items[0]

        searchterm = str(searchterm['external_urls'])[13:-2]
        features = spotify.audio_features(searchterm)
        dancey = features[0]['danceability']
        energyy = features[0]['energy']
        loudy = features[0]['loudness']
        speechey = features[0]['speechiness']
        acousty= features[0]['acousticness']
        instrumenty = features[0]['instrumentalness']
        valencey = features[0]['valence']
        tempoy = features[0]['tempo']
        #print( str(spotify.audio_features(searchterm)))
        print("Danceibility " + str(dancey) + " Energy " + str(energyy) + " Loudness " + str(loudy) + " Speechiness " + str(speechey))
        
        j += 1
    else:
        break
#songname = df.iloc[2].song
#artist = df.iloc[2].artist





    
    