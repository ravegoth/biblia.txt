from requests import *
import glob
import os
from bs4 import BeautifulSoup

links = [
    "http://www.bibliaortodoxa.ro/vechiul-testament/25/Facerea",
    "http://www.bibliaortodoxa.ro/vechiul-testament/32/Ie%C5%9Firea",
    "http://www.bibliaortodoxa.ro/vechiul-testament/47/Leviticul",
    "http://www.bibliaortodoxa.ro/vechiul-testament/59/Numerii",
    "http://www.bibliaortodoxa.ro/vechiul-testament/17/Deuteronomul",
    "http://www.bibliaortodoxa.ro/vechiul-testament/41/Iosua%20Navi",
    "http://www.bibliaortodoxa.ro/vechiul-testament/46/Judec%C4%83tori",
    "http://www.bibliaortodoxa.ro/vechiul-testament/71/Rut",
    "http://www.bibliaortodoxa.ro/vechiul-testament/66/I%20Regi",
    "http://www.bibliaortodoxa.ro/vechiul-testament/67/II%20Regi",
    "http://www.bibliaortodoxa.ro/vechiul-testament/68/III%20Regi",
    "http://www.bibliaortodoxa.ro/vechiul-testament/69/IV%20Regi",
    "http://www.bibliaortodoxa.ro/vechiul-testament/14/I%20Paralipomena",
    "http://www.bibliaortodoxa.ro/vechiul-testament/15/II%20Paralipomena",
    "http://www.bibliaortodoxa.ro/vechiul-testament/23/I%20Ezdra",
    "http://www.bibliaortodoxa.ro/vechiul-testament/58/Neemia",
    "http://www.bibliaortodoxa.ro/vechiul-testament/21/Esterei",
    "http://www.bibliaortodoxa.ro/vechiul-testament/42/Iov",
    "http://www.bibliaortodoxa.ro/vechiul-testament/65/Psalmi",
    "http://www.bibliaortodoxa.ro/vechiul-testament/63/Solomon",
    "http://www.bibliaortodoxa.ro/vechiul-testament/18/Ecclesiastul",
    "http://www.bibliaortodoxa.ro/vechiul-testament/9/C%C3%A2nt%C4%83ri",
    "http://www.bibliaortodoxa.ro/vechiul-testament/43/Isaia",
    "http://www.bibliaortodoxa.ro/vechiul-testament/31/Ieremia",
    "http://www.bibliaortodoxa.ro/vechiul-testament/64/Plangeri",
    "http://www.bibliaortodoxa.ro/vechiul-testament/33/Iezechiel",
    "http://www.bibliaortodoxa.ro/vechiul-testament/16/Daniel",
    "http://www.bibliaortodoxa.ro/vechiul-testament/60/Osea",
    "http://www.bibliaortodoxa.ro/vechiul-testament/3/Amos",
    "http://www.bibliaortodoxa.ro/vechiul-testament/56/Miheia",
    "http://www.bibliaortodoxa.ro/vechiul-testament/39/Ioil",
    "http://www.bibliaortodoxa.ro/vechiul-testament/6/Avdie",
    "http://www.bibliaortodoxa.ro/vechiul-testament/40/Iona",
    "http://www.bibliaortodoxa.ro/vechiul-testament/57/Naum",
    "http://www.bibliaortodoxa.ro/vechiul-testament/5/Avacum",
    "http://www.bibliaortodoxa.ro/vechiul-testament/73/Sofonie",
    "http://www.bibliaortodoxa.ro/vechiul-testament/2/Agheu",
    "http://www.bibliaortodoxa.ro/vechiul-testament/82/Zaharia",
    "http://www.bibliaortodoxa.ro/vechiul-testament/52/Maleahi",
    "http://www.bibliaortodoxa.ro/vechiul-testament/81/Tobit",
    "http://www.bibliaortodoxa.ro/vechiul-testament/45/Iudita",
    "http://www.bibliaortodoxa.ro/vechiul-testament/8/Baruh",
    "http://www.bibliaortodoxa.ro/vechiul-testament/20/Ieremia",
    "http://www.bibliaortodoxa.ro/vechiul-testament/1/3%20tineri",
    "http://www.bibliaortodoxa.ro/vechiul-testament/24/III%20Ezdra",
    "http://www.bibliaortodoxa.ro/vechiul-testament/74/Solomon",
    "http://www.bibliaortodoxa.ro/vechiul-testament/72/Ecclesiasticul",
    "http://www.bibliaortodoxa.ro/vechiul-testament/75/Susanei",
    "http://www.bibliaortodoxa.ro/vechiul-testament/7/Istoria%20Balaurului",
    "http://www.bibliaortodoxa.ro/vechiul-testament/49/I%20Macabei",
    "http://www.bibliaortodoxa.ro/vechiul-testament/50/II%20Macabei",
    "http://www.bibliaortodoxa.ro/vechiul-testament/51/III%20Macabei",
    "http://www.bibliaortodoxa.ro/vechiul-testament/54/Manase",
    "http://www.bibliaortodoxa.ro/noul-testament/55/Matei",
    "http://www.bibliaortodoxa.ro/noul-testament/53/Marcu",
    "http://www.bibliaortodoxa.ro/noul-testament/48/Luca",
    "http://www.bibliaortodoxa.ro/noul-testament/35/Ioan",
    "http://www.bibliaortodoxa.ro/noul-testament/26/Faptele%20Apostolilor",
    "http://www.bibliaortodoxa.ro/noul-testament/70/Romani",
    "http://www.bibliaortodoxa.ro/noul-testament/12/I%20Corinteni",
    "http://www.bibliaortodoxa.ro/noul-testament/13/II%20Corinteni",
    "http://www.bibliaortodoxa.ro/noul-testament/29/Galateni",
    "http://www.bibliaortodoxa.ro/noul-testament/19/Efeseni",
    "http://www.bibliaortodoxa.ro/noul-testament/28/Filipeni",
    "http://www.bibliaortodoxa.ro/noul-testament/10/Coloseni",
    "http://www.bibliaortodoxa.ro/noul-testament/76/I%20Tesaloniceni",
    "http://www.bibliaortodoxa.ro/noul-testament/77/II%20Tesaloniceni",
    "http://www.bibliaortodoxa.ro/noul-testament/78/I%20Timotei",
    "http://www.bibliaortodoxa.ro/noul-testament/79/II%20Timotei",
    "http://www.bibliaortodoxa.ro/noul-testament/80/Tit",
    "http://www.bibliaortodoxa.ro/noul-testament/27/Filimon",
    "http://www.bibliaortodoxa.ro/noul-testament/22/Evrei",
    "http://www.bibliaortodoxa.ro/noul-testament/30/Iacov",
    "http://www.bibliaortodoxa.ro/noul-testament/61/I%20Petru",
    "http://www.bibliaortodoxa.ro/noul-testament/62/II%20Petru",
    "http://www.bibliaortodoxa.ro/noul-testament/36/I%20Ioan",
    "http://www.bibliaortodoxa.ro/noul-testament/37/II%20Ioan",
    "http://www.bibliaortodoxa.ro/noul-testament/38/III%20Ioan",
    "http://www.bibliaortodoxa.ro/noul-testament/44/Iuda",
    "http://www.bibliaortodoxa.ro/noul-testament/4/Apocalipsa"
]


def capitole(link):
    # cate capitole are
    html = get(link).text
    soup = BeautifulSoup(html, 'html.parser')
    cap = len(soup.find_all("div", {"class": "css_navbar_cap"}))
    return cap


def titlu(link):
    # cum se numeste cartea
    html = get(link).text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all("div", {"class": "css_cat"})[0].getText()
    return title


def idcarte(link):
    # ce id are cartea
    id = link.split("/")[4]
    return id


def createlink(id, cap):
    # creeaza linkul pt extragerea versetelor
    return "http://www.bibliaortodoxa.ro/carte.php?id={}&cap={}".format(id, cap)


def verses(link, cap=""):
    # extrage versetele
    html = get(link).text
    soup = BeautifulSoup(html, 'html.parser')
    verses = ""
    for verseid in range(0, len(soup.findAll('table')[0].findAll('td'))//2):
        verses += str(cap) + "." + \
            str(1 + verseid) + ")\t" + \
            soup.findAll('table')[0].findAll('td')[1+verseid*2].text + "\n"
    return verses


def extragere():
    # proces principal
    for link in links:
        title = titlu(link)
        chapters = capitole(link)
        current_chapter = 1
        print("{} - {} capitole".format(titlu(link), capitole(link)))
        with open("biblia/{}.txt".format(title), "a", encoding="utf-8") as file:
            while current_chapter <= chapters:
                toparse = createlink(idcarte(link), current_chapter)
                print("Se extrag versete din {}".format(toparse))
                file.write(verses(toparse, current_chapter))
                current_chapter += 1

def concatenare():
    # face biblia un singur fisier
    text = ''
    search_dir = "biblia/"
    files = list(filter(os.path.isfile, glob.glob(search_dir + "*")))
    files.sort(key=lambda x: os.path.getmtime(x))
    for filename in files:
        with open(filename, 'r', encoding='utf8') as file:
            text += file.read()
    return text

extragere()
with open("biblia.txt", "w", encoding='utf8') as file:
    print(concatenare())
    file.write(concatenare())