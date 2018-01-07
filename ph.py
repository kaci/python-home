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
    for cont in conts:
        print(cont.a.text)

def ph_article():
    url = 'https://prohardver.hu/hir/kinaban_is_feltunt_a_nand_es_dram_arak_emelkedese.html'
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, 'lxml')

    cont_all = soup.find('div', itemprop = 'articleBody')
    conts = cont_all.find_all('p')
    for cont in conts:
        print(cont.text.strip().replace('[+]', ''))

if __name__ == '__main__':
    #ph_news(url)
    ph_article()
