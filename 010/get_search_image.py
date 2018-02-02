import requests
from bs4 import BeautifulSoup
import re

def filter_img(tag):
    return tag.has_attr('href')

def get_search_image(search):
    data = requests.get("https://www.google.com.au/search?q="+search+"&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjOmfyZ8YXZAhWJybwKHYIHBUEQ_AUICigB&biw=838&bih=924")
    soup = BeautifulSoup(data.content, 'html.parser')

    return soup.img['src']

print(get_search_image('dog'))
