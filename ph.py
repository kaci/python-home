from bs4 import BeautifulSoup
import requests

url  = 'https://prohardver.hu'
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'lxml')

conts = soup.find_all('li', class_ = 'content flc')
for cont in conts:
    print(cont.a.text)

url2 = 'https://prohardver.hu/hir/kinaban_is_feltunt_a_nand_es_dram_arak_emelkedese.html'
page2 = requests.get(url2)
data2 = page2.text
soup2 = BeautifulSoup(data2, 'lxml')

print('')

cont_all = soup2.find('div', itemprop = 'articleBody')
conts = cont_all.find_all('p')
for cont in conts:
    print(cont.text.strip())

