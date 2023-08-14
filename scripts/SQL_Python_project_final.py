#%%

# spotify sql project

# spotify data collection

import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn.preprocessing import MinMaxScaler
import csv
import os
import re
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials



# get rid of the https link from the playlist
def simplify_playlist_id(playlist):
    """
    
    Takes the playlists hyperlink, and strips the hyperlink features and
    returns the unique playlist id
    
    """
    
    if match:= re.match(r"https://open.spotify.com/playlist/(.*)\?", playlist):
        playlist = match.groups()[0]
        
    else:
        raise ValueError("Expected format: https://open.spotify.com/playlist/...")
        
    return playlist

class Get_Spotify_Meta_Data():
    
    """
    
    This class takes in the client_id, the playlist id the user wants to
    work with, and the user credentials from the .env file. 
    The class has 2 methods, get_genre and get_playlist_tracks. 
        
    """
    def __init__(self, username, playlist_id, sp):
        self.username = username
        self.playlist_id = playlist_id
        self.sp = sp
    
    def get_genre(self, track_id):
        
        """
        
        Since Spotify doesn't store genre data for each individual song, 
        we have to look at the artists genre, and connect that to the rest
        of the songs metadata. This method takes in a song (track_id), looks up the
        genres the artist works in, then associates the song with those genres.
        
        """
        
        track_data = sp.track(track_id)
        
        artist_ids = []
        
        for artist in track_data["artists"]:
            artist_ids.append(artist["id"])
        
        artists_data = sp.artists(artist_ids)
        
        genres = []
        
        for artist in artists_data["artists"]:
            genres += artist["genres"]
        
        genres = set(genres) # removes duplicates
        
        return genres

    def get_playlist_tracks(self):
        
        """
        
        This method loops through all the songs inside the users playlist. 
        Metadata such as track name, genre, danceability, etc are all gathered
        and stored in a dataframe.
        
        """
        
        results = sp.user_playlist_tracks(self.username , self.playlist_id)
        tracks = results['items']
        
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        results = tracks
        
        playlist_tracks_id = []
        playlist_tracks_titles = []
        playlist_tracks_artists = []
        playlist_tracks_first_artists = []
        playlist_tracks_first_release_date = []
        playlist_tracks_popularity = []
          
        for i in range(len(results)):
            print(i) # Counter
            
            # the first track is used to set the columns/metadata types
            if i == 0:
                playlist_tracks_id = results[i]['track']['id']
                playlist_tracks_titles = results[i]['track']['name']
                playlist_tracks_first_release_date = results[i]['track']['album']['release_date']
                playlist_tracks_popularity = results[i]['track']['popularity']
                genre = self.get_genre(playlist_tracks_id)
                print(genre)
                
    
                artist_list = []
                for artist in results[i]['track']['artists']:
                    artist_list= artist['name']
                playlist_tracks_artists = artist_list
                
    
                features = self.sp.audio_features(playlist_tracks_id)
                
                features_df = pd.DataFrame(data=features, columns=features[0].keys())
                features_df['title'] = playlist_tracks_titles
                features_df['all_artists'] = playlist_tracks_artists
                features_df['popularity'] = playlist_tracks_popularity
                features_df['release_date'] = playlist_tracks_first_release_date
                features_df['genre'] = [genre]
                features_df = features_df[['id', 'title', 'all_artists', 'popularity', 'release_date', 
                                           'genre', 'danceability', 'energy', 'key', 'loudness',
                                           'mode', 'acousticness', 'instrumentalness',
                                           'liveness', 'valence', 'tempo',
                                           'duration_ms', 'time_signature']]
                
                continue
            
            # populating the dataframe with the rest of the data
            else:
                try:
                    playlist_tracks_id = results[i]['track']['id']
                    playlist_tracks_titles = results[i]['track']['name']
                    playlist_tracks_first_release_date = results[i]['track']['album']['release_date']
                    playlist_tracks_popularity = results[i]['track']['popularity']
                    genre = self.get_genre(playlist_tracks_id)
                    print(genre)
                    
                    
                    artist_list = []
                    for artist in results[i]['track']['artists']:
                        artist_list= artist['name']
                    playlist_tracks_artists = artist_list
                    features = sp.audio_features(playlist_tracks_id)
                    new_row = {'id':[playlist_tracks_id],
                   'title':[playlist_tracks_titles],
                   'all_artists':[playlist_tracks_artists],
                   'popularity':[playlist_tracks_popularity],
                   'release_date':[playlist_tracks_first_release_date],
                   'genre': [genre],
                   'danceability':[features[0]['danceability']],
                   'energy':[features[0]['energy']],
                   'key':[features[0]['key']],
                   'loudness':[features[0]['loudness']],
                   'mode':[features[0]['mode']],
                   'acousticness':[features[0]['acousticness']],
                   'instrumentalness':[features[0]['instrumentalness']],
                   'liveness':[features[0]['liveness']],
                   'valence':[features[0]['valence']],
                   'tempo':[features[0]['tempo']],
                   'duration_ms':[features[0]['duration_ms']],
                   'time_signature':[features[0]['time_signature']]
                   }
                    
                    dfs = [features_df, pd.DataFrame(new_row)]
    
                    # add in the new line
                    features_df = pd.concat(dfs, ignore_index = True)
                except:
                    continue
                    
        return features_df
    

if __name__ == "__main__":
        
    # load in the client_id and secret_id from the .env file
    load_dotenv()
    
    CLIENT_ID = os.getenv("CLIENT_ID", "")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
    
    
    # the playlists
    playlist_id_noah = 'https://open.spotify.com/playlist/1R7XtjKBfJbkT3RciGcyQ4?si=f19120e07b754aea'
    playlist_id_zsoli = 'https://open.spotify.com/playlist/7bqKXUIyL3jLmHRJbcGd8k?si=01a5b30fa52d49abspotify:playlist:7bqKXUIyL3jLmHRJbcGd8k'
    
    #strip away the https
    noahs_playlist = simplify_playlist_id(playlist_id_noah)
    zsolis_playlist = simplify_playlist_id(playlist_id_zsoli)
    
    
    client_credentials_manager = SpotifyClientCredentials(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    # gather my data
    Noahsdata = Get_Spotify_Meta_Data(CLIENT_ID, playlist_id_noah, sp)
    noahs_music = Noahsdata.get_playlist_tracks()
    
    # export to csv
    noahs_music.to_csv('noahs_music.csv', sep='\t')
    
    # gather zsoli's data
    Zsolisdata = Get_Spotify_Meta_Data(CLIENT_ID, playlist_id_zsoli, sp)
    zsolis_music = Zsolisdata.get_playlist_tracks()
    
    # export to csv
    zsolis_music.to_csv('zsolis_music.csv', sep= '\t')
    
    print('finished!')
    
    

