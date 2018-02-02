
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
from bs4 import BeautifulSoup

def get_coin_data():
    try:
        data = requests.get("https://coinmarketcap.com/")
    except Exception as exc:
        print(exc)
        data = None
    return data

def parse_data(data):
    soup = BeautifulSoup(data.content, 'html.parser')
    coins = [Coin(coin) for coin in soup.tbody.find_all('tr', class_="")]

    return coins

def get_coins():
    return parse_data(get_coin_data())

def get_coin(coin):
    for c in get_coins():
        if c._name == coin:
            return [c]
    return []


if __name__ == '__main__':
    coins = get_coins()
    print(coins)
"""    for c in coins:
        print("Name: " + c._name + ", Price: " + c._price + \
                ", Change(24h): " + c._change)"""

    
    
