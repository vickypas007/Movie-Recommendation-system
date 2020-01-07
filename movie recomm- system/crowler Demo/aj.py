from bs4 import BeautifulSoup
import requests
import imdb

# ia =imdb.IMDb()
source = requests.get("https://www.rottentomatoes.com/m/aquaman_2018/reviews/?sort=rotten")
soup = BeautifulSoup(source.content,'html.parser')
print(soup.prettify())
