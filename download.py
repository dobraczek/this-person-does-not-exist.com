from urllib import request
from urllib.request import Request, urlopen
from PIL import Image
from datetime import datetime
import json
import requests
import os
import time

# nastavneni

n_count = 5; # pocet polozek 
n_path = 'download' # adresar
n_gender = 'male' # pohlavi
n_age = '19-25' # vekova kategorie (19-25, )
n_entit = 'latino_hispanic' # barva pleti

dt = datetime.now()
n_date = datetime.timestamp(dt)


# stahovani

for x in range(n_count):

    # zjistit obrazek - json
    request_site = Request("https://this-person-does-not-exist.com/en?new=" + str(n_date) + "&gender=" + n_gender + "&age=" + n_age + "&etnic=" + n_entit, headers={"User-Agent": "Mozilla/5.0"})
    webpage = urlopen(request_site).read()

    # zpracovat json
    data  = json.loads(webpage)
    img = 'https://this-person-does-not-exist.com/' + data['src']

    # zjistit nazev souboru
    if img.find('/'):
        imgname = img.rsplit('/', 1)[1]

    # stahnout obrazek
    response = requests.get(img)
    open(n_path + "/" + imgname, "wb").write(response.content)

    # oriznout obrazek
    im = Image.open(n_path + "/" + imgname)

    # zjistit velikost a upravit obrazek
    width, height = im.size
    im1 = im.crop((60, 60, 904, 904))
    im1.save(n_path + "/_" + imgname)

    # smazat puvodni
    os.unlink(n_path + "/" + imgname)

    # pockam 1s
    time.sleep(1)

    # zobrazeni nazvu stazene fotografie
    print(imgname)