#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

url  = 'https://prohardver.hu'

def ph_news(url):
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, 'lxml')
    
    conts = soup.find_all('li', class_ = 'content flc')
    return [(x.a.text, x.a['href']) for x in conts]
        
def ph_article():
    url = 'https://prohardver.hu/teszt/ajanlatok_tavasz_elejere/notebookok.html'
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, 'lxml')

    cont_all = soup.find('div', itemprop = 'articleBody')
    conts = cont_all.find_all('p')
    return [x.text.strip().replace('[+]', '') for x in conts]

if __name__ == '__main__':
    #print(ph_news(url))
    print(ph_article())
