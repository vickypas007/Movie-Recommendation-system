import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import cosine_similarity

# mydb = mysql.connector.connect(host='localhost',user='root',password='',database='movie')
# print("database connected")

u_cols = ['user_id', 'movieid', 'rating']
df = pd.read_csv('rating1.csv')
print(df.head())
print()
movie_title= pd.read_csv("movietitle.csv")
print(movie_title.head())

print()
df= pd.merge(df,movie_title,on='movieid')
print(df)

data=df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
print(data)

print(df.groupby('title')['rating'].count().sort_values(ascending=False).head())
print()
rating =pd.DataFrame(df.groupby('title')['rating'].mean())
print(rating.head())
print()

rating['num of rating']=pd.DataFrame(df.groupby('title')['rating'].count())
print(rating.head())

plt.figure(figsize=(10,4))
rating['num of rating'].hist(bins=70)
plt.show()

plt.figure(figsize=(10,4))
rating['rating'].hist(bins=70)
plt.show()
g=sns.jointplot(x='rating',y='num of rating',data=rating,alpha=0.5)
print()
print()
moviemat =df.pivot_table(index='userid',columns='title',values='rating')
print(moviemat.head())

print()
print(rating.sort_values('num of rating',ascending=False).head(10))

avenger_user_rating = moviemat['Avenger: Infinity war']
# thor_user_rating = moviemat['Thor regnarok']
print(avenger_user_rating)

print()
# analysing correlation with similar movies

similar_to_avenger =(moviemat.corrwith(avenger_user_rating))
# similar_to_thor = moviemat.corrwith(thor_user_rating)
# print(similar_to_aquaman)



corr_avenger =pd.DataFrame(similar_to_avenger, columns =['Correlation'])
corr_avenger.dropna(inplace = True)
print(corr_avenger.head())
print("upto corr_aquaman\n \n ")



print(corr_avenger.sort_values('Correlation',ascending=False).head(10))
print()

corr_avenger = corr_avenger.join(rating['num of rating'])

print(corr_avenger.head())

p = corr_avenger[corr_avenger['num of rating'] >2].sort_values('Correlation', ascending=False)

print(p)
