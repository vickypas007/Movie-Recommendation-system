import requests
from bs4 import BeautifulSoup
import wget


def download_links(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    fileNo = 1
    index = 0
    for link in soup.findAll('a'):
        href = link.get('href')
        index += 1
        if (href == "index.html" or index % 2 == 0):
            continue
        href = "https://www.aukdc.edu.in/fis/" + href
        print(href)
        # if(href != None and len(href) > 4):
        #   extensionStr = href[-13] + href[-12] + href[-11] + href[-10]
        #  if(extensionStr == ".php"):
        #     print(href)
        wget.download(href,out=r'C:\Users\Vicky\Desktop\dbFaculty\ '+str(fileNo)+'.pdf')
        fileNo += 1


download_links('https://www.aukdc.edu.in/fis/facprofile_inddept.php?ch=IST&chh=College of Engineering, Guindy')