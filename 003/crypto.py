
class Coin(object):
    def __init__(self, data):
        self._data = data
        self._name = self.get_name()
        self._price = self.get_price()
        self._change = self.get_change()
    
    def get_name(self):
        return self._data.find(class_='currency-name-container').get_text()       

    def get_price(self):
        return self._data.find(class_='price').get_text()
    
    def get_change(self):
        return self._data.find(class_='percent-24h').get_text()

import requests

page = requests.get("https://coinmarketcap.com/")

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify().encode('utf-8'))

coins = [Coin(coin) for coin in soup.tbody.find_all('tr', class_="")]

for c in coins:
    print("Name: " + c._name + ", Price: " + c._price + \
            ", Change(24h): " + c._change)

    
    
