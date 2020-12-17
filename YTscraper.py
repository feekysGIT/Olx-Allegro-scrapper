import requests
from bs4 import BeautifulSoup
import webbrowser
import time

SERVER_URL = "http://192.168.0.105:5000/"
URL = 'https://www.olx.pl/oferta/szafa-przesuwna-245cm-rio-3-trzy-kolory-z-lustrem-CID628-IDETP5q.html'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
CENA_KTOREJ_OCZEKUJECIE = 1410
def check_price():
    while True:
        try:
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            price = soup.findAll("strong", {"class": "pricelabel__value not-arranged"})[0].string
            converted_price = int(price[:-2].strip())


            print(soup.title.string)
            print("Aktualna Cena Wynosi: "+ str(converted_price) +" ZŁ")
            print('Checking...')

            
            if converted_price <= CENA_KTOREJ_OCZEKUJECIE:
                print("CENA ZOSTAŁA OBNIŻONA!")
                webbrowser.register('chrome', None,
                                webbrowser.BackgroundBrowser(
                                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open_new(URL)

            time.sleep(2)
        except (ValueError):
            pass
        except (IndexError):
            pass

check_price()
