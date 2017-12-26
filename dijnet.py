#!/usr/bin/python3

'''
Dijnet számláit - a böngészést szimulálva - pdf formátumban letöltő szkript.
Lassan dolgozik, a time.sleep()-el várakozik egy-egy új oldal letöltésére.
'''

import getpass, argparse, time, logging, os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dload_dir = input("Kérlek add meg a számlák letöltési helyét: ")
if not os.path.exists(dload_dir):
    os.makedirs(dload_dir)
    
# set firefox auto-download
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", dload_dir)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
profile.set_preference("pdfjs.disabled", True)

# get login username and password
parser = argparse.ArgumentParser(description = "login to dijnet")
args = parser.parse_args()
args.username = input("Kérlek add meg a díjnet felhasználónevet: ")
args.password = getpass.getpass("Kérlek add meg a díjnet jelszót: ")

# set basic logging
logging.basicConfig(filename = 'dijnet.log', level = logging.INFO)

# open firefox and get page
driver = webdriver.Firefox(firefox_profile = profile)
driver.get("https://www.dijnet.hu/ekonto/control/welcome")
assert "dijnet.hu ... a neten csenget" in driver.title

# fill login form
elem = driver.find_element_by_name('username')
elem.send_keys(args.username)
elem = driver.find_element_by_name('password')
elem.send_keys(args.password)
elem.send_keys(Keys.RETURN)
time.sleep(3)

# find Számlakeresés, and click
driver.find_element_by_link_text(u'Számlakeresés').click()
time.sleep(1)

# find Keresés, and click
driver.find_element_by_name('button_gen_N10151').click()
time.sleep(1)

# page source push to beautifulsoup and find links
html = driver.page_source
soup = BeautifulSoup(html, "lxml")

# find links, unique, and sorted
links = [i['href'] for i in soup.find_all("a", {"class":"td_link"})]
slinks = [link for link in sorted(list(set(links))) if 'szamlaszam' in link]

# walk on all accounts
for slink in slinks:
    # get account link
    driver.get('https://www.dijnet.hu' + slink)
    driver.find_element_by_link_text(u'Letöltés').click()    
    time.sleep(1)
    
    # download pdf
    driver.find_element_by_class_name("xt_link__download").click()    
    logging.info(slink)
        
    # go back list of accounts
    driver.find_element_by_class_name("xt_link_cell__title").click()
    time.sleep(1)

# logout and close firefox
driver.find_element_by_xpath('''//button[@onclick="location.href='/ekonto/control/logout'"]''').click()
driver.close()
