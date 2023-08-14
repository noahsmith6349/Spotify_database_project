# Spotify_data_project
 Spotify playlist project

## About this project:

### My friend Zsoli and I have very different tastes in music. We wanted to create a spotify playlist that combines
### some of our music based on the following criteia:

### Primary requirements:
### Zsoli's:
### - no rock
### - maximize energy and danceability from spotify's metadata

### Noah's: 
### - keep all jazz
### - no country
### - keep all indie music

### Secondary requirements:
### - prefer songs less than 4 minutes

As time goes on, I plan to add to this project by making an algorithm that reccomends songs to add to our shared playlist. But for now, the scripts are as follows:

## SQL_Python_projject_final.py
- This script gathers the spotify data from two set playlists.
- It takes my Spotify api client credientials (stored in the .env file) and collects all the meta data from the songs in the playlist.
- THe output are two csv's; one with my playlist meta-data, and one with Zsoli's playlist meta-data.

- The .env file uploaded here is blank for privacy reasons. You can reproduce this project by inputting your own client credentials. *


## Spotify_playlist_merging.sql
- This sql script combines the two playlists and filters all the data according to the requirements described above. The output is the 
"combined_music___.csv" , which will be used to produce the radar charts

## radar_charts.py
- This file produces radar charts for both the original csv's, as well as the combined csv. Maybe our tastes in music aren't so different after all!





