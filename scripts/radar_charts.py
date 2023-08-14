
# Creating a Radar Chart 

from matplotlib import pyplot as plt
from math import pi as pi
import csv
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

path = r'C:\Python Learning\Data Science\SQL_Spotify_project\combined_music_202308121935.csv'
df = pd.read_csv(path)

# =============================================================================
# columns_to_drop = ['popularity', 'tempo','duration_ms','song_count', 
#                    'id', 'title', 'all_artists', 'release_date', 'genre', 
#                    'time_signature', ]
# df.drop(columns = columns_to_drop, inplace=True)
# =============================================================================


music_feature = df[['danceability','energy','loudness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms']]
min_max_scaler = MinMaxScaler()
music_feature.loc[:] = min_max_scaler.fit_transform(music_feature.loc[:])


# normalizing the data

min_max_scaler = MinMaxScaler()
music_feature.loc[:] = min_max_scaler.fit_transform(music_feature.loc[:])

# Creating a Radar Chart 

# plot size
fig=plt.figure(figsize=(12,8))

# convert column names into a list
categories=list(music_feature.columns)
# number of categories
N=len(categories)

# create a list with the average of all features
value=list(music_feature.mean())

# repeat first value to close the circle
# the plot is a circle, so we need to "complete the loop"
# and append the start value to the end.
value+=value[:1]
# calculate angle for each category
angles=[n/float(N)*2*pi for n in range(N)]
angles+=angles[:1]

# plot
plt.polar(angles, value)
plt.fill(angles,value,alpha=0.3)

# plt.title('Discovery Weekly Songs Audio Features', size=35)

plt.xticks(angles[:-1],categories, size=15)
plt.yticks(color='grey',size=15)
plt.title('combined_music')
plt.show()
print(N)


#%% now compare this radar chart to the data from each individual csv


#%% Noah's music

from matplotlib import pyplot as plt
from math import pi as pi
import csv
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

noah_path = r"C:\Users\Noah\Downloads\noahs_music.csv"

df = pd.read_csv(noah_path)

# =============================================================================
# columns_to_drop = ['popularity', 'tempo','duration_ms','song_count', 
#                    'id', 'title', 'all_artists', 'release_date', 'genre', 
#                    'time_signature', ]
# df.drop(columns = columns_to_drop, inplace=True)
# =============================================================================
df.columns

music_feature = df[['danceability','energy','loudness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms']]
min_max_scaler = MinMaxScaler()
music_feature.loc[:] = min_max_scaler.fit_transform(music_feature.loc[:])


# normalizing the data

min_max_scaler = MinMaxScaler()
music_feature.loc[:] = min_max_scaler.fit_transform(music_feature.loc[:])

# Creating a Radar Chart 

# plot size
fig=plt.figure(figsize=(12,8))

# convert column names into a list
categories=list(music_feature.columns)
# number of categories
N=len(categories)

# create a list with the average of all features
value=list(music_feature.mean())

# repeat first value to close the circle
# the plot is a circle, so we need to "complete the loop"
# and append the start value to the end.
value+=value[:1]
# calculate angle for each category
angles=[n/float(N)*2*pi for n in range(N)]
angles+=angles[:1]

# plot
plt.polar(angles, value)
plt.fill(angles,value,alpha=0.3)

# plt.title('Discovery Weekly Songs Audio Features', size=35)

plt.xticks(angles[:-1],categories, size=15)
plt.yticks(color='grey',size=15)
plt.title('Noahs music')
plt.show()
print(N)

#%%
# Zsoli's music


from matplotlib import pyplot as plt
from math import pi as pi
import csv
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

zsoli_path = r"C:\Users\Noah\Downloads\zsolis_music.csv"

df = pd.read_csv(zsoli_path)

# =============================================================================
# columns_to_drop = ['popularity', 'tempo','duration_ms','song_count', 
#                    'id', 'title', 'all_artists', 'release_date', 'genre', 
#                    'time_signature', ]
# df.drop(columns = columns_to_drop, inplace=True)
# =============================================================================
df.columns

music_feature = df[['danceability','energy','loudness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms']]
min_max_scaler = MinMaxScaler()
music_feature.loc[:] = min_max_scaler.fit_transform(music_feature.loc[:])


# normalizing the data

min_max_scaler = MinMaxScaler()
music_feature.loc[:] = min_max_scaler.fit_transform(music_feature.loc[:])

# Creating a Radar Chart 

# plot size
fig=plt.figure(figsize=(12,8))

# convert column names into a list
categories=list(music_feature.columns)
# number of categories
N=len(categories)

# create a list with the average of all features
value=list(music_feature.mean())

# repeat first value to close the circle
# the plot is a circle, so we need to "complete the loop"
# and append the start value to the end.
value+=value[:1]
# calculate angle for each category
angles=[n/float(N)*2*pi for n in range(N)]
angles+=angles[:1]

# plot
plt.polar(angles, value)
plt.fill(angles,value,alpha=0.3)

# plt.title('Discovery Weekly Songs Audio Features', size=35)

plt.xticks(angles[:-1],categories, size=15)
plt.yticks(color='grey',size=15)
plt.title('Zsolis music')
plt.show()
print(N)











