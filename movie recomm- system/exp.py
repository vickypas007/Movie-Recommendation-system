import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='movie')
print('connected')
movieid =mydb.cursor()

movieid.execute("select movieid from movielist")
movieid=movieid.fetchall()
print(movieid)
userid=mydb.cursor()
userid.execute("select userid, movieid ,rate from rating limit 5")
for i in userid:
    print(i)

movie_title =mydb.cursor()
movie_title.execute("select movieid,title from movielist limit 5")
for mov in movie_title:
    print(mov)

print(movieid.groupby('movie_title')['userid'].mean().sort_values(ascending=False).head())

# df= pd.merge(userid,movie_title,on='movieid')
# for ff in df:
#     print(ff)



