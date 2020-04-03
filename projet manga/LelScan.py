import requests
import urllib.request
import os
from PIL import Image
import shutil
from bs4 import BeautifulSoup

LeSite = "https://www.lelscan-vf.com/"

os.chdir(r"C:\Users\youne")

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens=image(soup)
    return [soup,ListeLiens]


def image(soup):
    ListeLiens = []
    Image = soup.findAll('img')
    for elt in Image:
        if 'class' in elt.attrs and elt['class']==["img-responsive"]:
            photo = elt['data-src']
            ListeLiens.append(photo)
    return ListeLiens


def chapitresuivant(soup,url):
    resteURL=RESTE(url)
    numero=numeroUrl(url)
    NextUrl=resteURL+str(numero+1)
    a=str(NextUrl)
    if image(soup) == []:
        NextUrl = "Fin du Manga"
        print(NextUrl)
    else:
        print(NextUrl)
    return NextUrl

def numeroUrl(url):
    bac=url.split('/')[-1]
    return int(bac)


def RESTE(url):
    url2 = url.split(str(numeroUrl(url)))[0]
    return url2