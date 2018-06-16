import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('tmdb-movies.csv')

df = df[['popularity','release_year','genres']]
popular = np.percentile(df['popularity'],99)
df = df.query('popularity > {}'.format(popular))
df['genre_1'], df['genre_2'],df['genre_3'],df['genre_4'],df['genre_5'], = df['genres'].str.split('|').str

year = df['release_year'].append(df['release_year']).append(df['release_year']).append(df['release_year']).append(df['release_year'])
genre = df['genre_1'].append(df['genre_2']).append(df['genre_3']).append(df['genre_4']).append(df['genre_5'])

df = pd.DataFrame()
df['Year'] = year
df['Genre'] = genre
df.dropna(inplace = True)
df['count']= 1

df = df.groupby(['Year','Genre'],as_index=False).sum()
df = df.pivot(index='Year',columns='Genre')
df.fillna(0, inplace = True)
df.columns = df.columns.droplevel(0)

df.query('Year >= 1995').sum().plot(kind='bar',figsize=(12,12))
plt.xlabel('Genre',fontsize=18)
plt.ylabel('Counts',fontsize=18)
plt.title('Counts For Popular Movies By Genre - Post 1995',fontsize=18)
plt.savefig('Counts For Popular Movies By Genre - Post 1995.png');

df.query('Year < 1995').sum().plot(kind='bar',figsize=(12,12))
plt.xlabel('Genre',fontsize=18)
plt.ylabel('Counts',fontsize=18)
plt.title('Counts For Popular Movies By Genre - Pre 1995',fontsize=18);
plt.savefig('Counts For Popular Movies By Genre - Pre 1995.png');

df.plot(kind='barh',stacked=True,figsize=(12,12));
plt.xlabel('Counts',fontsize=18)
plt.ylabel('Year',fontsize=18)
plt.title('Movie Genre Count Over Years - Stacked Bar Chart',fontsize=18)
plt.savefig('Movie Genre Count Over Years - Stacked Bar Chart.png');

df.plot(kind='line',stacked=True,figsize=(12,12));
plt.xlabel('Year',fontsize=18)
plt.ylabel('Counts',fontsize=18)
plt.title('Movie Genre Count Over Years - Stacked Line Chart',fontsize=18)
plt.savefig('Movie Genre Count Over Years - Stacked Line Chart.png');
