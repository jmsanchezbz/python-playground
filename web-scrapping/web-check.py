#!/usr/bin/env python3

import json
import urllib
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url_fitxa = "https://seu.conselldemallorca.net/es/ficha?key=90916"

page = requests.get(url_fitxa)
#print(page.text)

def check(code, url):
    page = requests.get(url_fitxa)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="titulotramitedocu")
    #results = soup.find_next("h1", class_="titulotramitedocu")
    print(results.h1.text)
    return True

def check2():
    browser = webdriver.Firefox()

    browser.get(url_fitxa)
    assert 'Concurs' in browser.title

    elem = browser.find_element(By.ID, 'titulotramitedocu')
    print("Element text: " + elem.text)
    elem = browser.find_element(By.CLASS_NAME, 'titulotramitedocu')
    print("Element text: " + elem.text)
    browser.quit()


result = check2()
print("Checking " + str(result))

url = "https://emap.conselldemallorca.cat/documents/7858057/8329905/cimplaces.json"

#response = urllib.request.urlopen(url)
#data = json.loads(response.read())
"""
r = requests.get(url)
print(r.text)
"""

#data = r.json()
#print(data)
#for i in data:
#    print(i)
    #    print(str(i).replace("\'", "\""))
#    o = json.loads(str(i).replace("\'", "\""))
#    print(o['Codi'])
#    exit()

#print(r.json())
#print(data)

