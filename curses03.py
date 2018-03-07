#!/usr/bin/python3
# encoding: utf-8
  
import curses, requests, textwrap
from curses import panel
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProH(object):
    
    def __init__(self, url):
        self.url = url
    
    def megtobb(url):
        browser = webdriver.PhantomJS()
        browser.get(url)
 
        browser.find_element_by_link_text("Még több anyag...").click()
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, \
        '''//*[@onclick="javascript:ajax_GetMoreContent('/fooldal/index.html?ajax=1&page=2', this); return false;"]''')))
        
        page = request.get(url)
        browser.close()
    
    def news(url):
        page = requests.get(url)
        data = page.text
        soup = BeautifulSoup(data, 'lxml')
    
        conts = soup.find_all('li', class_ = ['content flc', 'content flc feat'])
        return [(x.a.text, x.a['href']) for x in conts]
        
    def article(art_url):
        art_url = 'https://prohardver.hu' + art_url
        art_page = requests.get(art_url)
        art_data = art_page.text
        art_soup = BeautifulSoup(art_data, 'lxml')

        cont_all = art_soup.find('div', itemprop = 'articleBody')
        conts = cont_all.find_all('p')        
        return [x.text.strip() for x in conts]
        
class Menu(object):                                                          

    def __init__(self, items, stdscreen):
        self.window = stdscreen.subwin(0,0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items        

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items)-1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = '{}'.format(item[0])
                self.window.addstr(index, 2, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                self.disp_text(ProH.article(self.items[self.position][1]))

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)
            
            elif key == ord('q'):
                break

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()
    
    def disp_text(self, art_text):
        self.panel.top()
        self.panel.show()
        self.window.clear()
        
        c = 0
        
        while c == 0:
            self.window.refresh()
            text = ' '.join(t for t in art_text if '+' not in t)
            self.window.addstr(1, 1, textwrap.fill(text, 110, subsequent_indent=' '))
            
            # Store the key value in the variable `c`
            c = self.window.getch()
        
        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

class MyApp(object):

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0) # no cursor

        submenu_items = []
        submenu = Menu(submenu_items, self.screen)

        main_menu_items = [(x[0], x[1]) for x in ProH.news('https://prohardver.hu/index.html?ajax=1&page=1')]
        main_menu = Menu(main_menu_items, self.screen)
        main_menu.display()

if __name__ == '__main__':
    curses.wrapper(MyApp)
