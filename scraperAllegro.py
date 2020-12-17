import requests
from bs4 import BeautifulSoup
import webbrowser
import time

SERVER_URL = "http://192.168.0.105:5000/"
URL = 'https://allegro.pl/oferta/wiszace-gwiazdy-kurtyna-lampki-choinkowe-138-led-k-9941463515?bi_m=mpage&'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
CENA_KTOREJ_OCZEKUJECIE = 30
while True:
    try:
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all('span')[17].get_text().strip()[:-1]
        title = soup.title

        print(title.string[:-29])
        print(price)
        if int(price) <= CENA_KTOREJ_OCZEKUJECIE:
            print("CENA ZOSTAŁA OBNIŻONA!")
            webbrowser.register('chrome', None,
                            webbrowser.BackgroundBrowser(
                            "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new(URL)
            break

        
        time.sleep(2)
    except (ValueError):
            pass
    except (IndexError):
            pass


