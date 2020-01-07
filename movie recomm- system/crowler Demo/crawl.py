from bs4 import BeautifulSoup as soup
from  urllib.request import urlopen as uReg
import re
my_url ='https://www.rogerebert.com/reviews/page/5'

uClient =uReg(my_url)
page_html =uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")

containers =page_soup.findAll("div",{"id": "review-list"})
# print(len(containers))

# print(soup.prettify(containers[0]))

container = containers[0]

titl =container.findAll("figure",{"class":"movie review"})
# for item in title:
#     print(item.text)

filename ="output1.csv"
f=open(filename,"w")

headers="Title, Actor_name,Release_Date\n"
f.write(headers)

# for container in containers:

title_name= container.findAll("figure",{"class":"movie review"})
for item in title_name:
    title=item.text.strip()

    #print(title)
    # #string parsing
    trim_title=''.join(title.split(" "))
    print(re.sub("\s+", ",", trim_title.strip()+"\n"))
    f.write(re.sub("\s+", ",", trim_title.strip()+"\n")+"\n")

f.close()













