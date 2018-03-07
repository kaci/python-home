#!/usr/bin/python3
# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.PhantomJS()
browser.get("https://prohardver.hu/index.html")
 
browser.find_element_by_link_text("Még több anyag...").click()
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, \
'''//*[@onclick="javascript:ajax_GetMoreContent('/fooldal/index.html?ajax=1&page=2', this); return false;"]''')))

browser.close()
