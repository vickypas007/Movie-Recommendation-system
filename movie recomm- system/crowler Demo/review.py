from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReg
import re

my_url ="https://www.rottentomatoes.com/m/thor_ragnarok_2017/reviews/?page=5&type=user&sort="

uClient =uReg(my_url)
page_html =uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
# print(soup.prettify())

containers =page_soup.findAll("div", {"class" :"user_review"})
# print(len(containers))


filename ="review2.csv"
f = open(filename,"w")

headers ="Reviews\n"
f.write(headers)

for item in containers:
    text=item.text.strip()



    # rat = text.replace("\\,.;" " ")
    mystring = text.replace(",", "")
    # print(mystring)
    # f.write(mystring +"\n")

    my_str = " ".join([a.strip() for a in mystring.split("\n") if a])
    print('"' + my_str + '"')
    f.write('"' + my_str + '"' + "\n")


    # f.close()







