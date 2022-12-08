#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlparse

#from selenium.webdriver.chrome.options import Options
#from bs4 import BeautifulSoup
import sys
import time
#import os
import csv
import urllib.request
import json
#import requests
import wget
import unittest
import sys
#from collections import defaultdict

URL_json_cim = "https://emap.conselldemallorca.cat/documents/7858057/8329905/cimplaces.json"
URL_json_ent = "https://emap.conselldemallorca.cat/documents/7858057/8329905/ajplaces.json"
idProcediment = 90659


def download(url, filename):
    r = wget.download(url, filename)

def load_json(filepath):
    with open(filepath) as jsonFile:
        data = json.load(jsonFile)
    return data

def obtain_json(url):
    with urllib.request.urlopen(url) as url1:
        data = json.load(url1)
    return data

"""
    verify_procediment
    return [seu_codi_title_ok, seu_link_app, seu_err_msg]
"""


def verify_procediment(codi, idProcediment):
    isOk = False
    result = []
    URL_seu = "https://seu.conselldemallorca.net/ca/fitxa?key="
    url = URL_seu + str(idProcediment)

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    link = ''

    try:
        if (idProcediment == 0):
            print("verify_procediment: " + str(idProcediment))
            result = [True, '', '']
            return

        # Check if the scheme and netloc components are not empty
        print("verify_procediment: " + url)
        result = urlparse(url)
        if result.scheme and result.netloc:
            print("check url: " + result.scheme + " " + result.netloc)
            driver.get(url)
            driver.implicitly_wait(20)
            title_css_selector = "div.titulotramitedocu#titulotramitedocu > h1"
            elem = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, title_css_selector))
            )
            #elem = driver.find_element(By.CSS_SELECTOR, title_css_selector)
            #print(elem.text)

            if (codi in elem.text):
                isOk = True

            link_procediment = "a.btn.btn-lg.btn-primary.botonrealizartramit"
            link_elem = driver.find_elements(By.CSS_SELECTOR, link_procediment)
            link = link_elem[0].get_attribute("href")
        else:
            print("Invalid URL")
        result = [isOk, link, ""]
    except TimeoutException as ex:
        result = [isOk, link, str(ex)]
    except:
        e = sys.exc_info()[0]
        result = [isOk, link, str(e)]
    finally:
        driver.quit()
        print("verify_procediment: "+str([codi, idProcediment]+result))
        return result


"""
    verify_convocatoriaapp
    return [app_codi_ok, app_err_msg]
"""


def verify_apppage(codi, url):
    isOk = False
    result = []

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    try:
        if(url == ''):
            result = [True, '']
            return

        # Check if the scheme and netloc components are not empty
        result = urlparse(url)
        if result.scheme and result.netloc:
            driver.get(url)
            driver.implicitly_wait(20)
            title_css_selector = "h3.d-inline-flex.justify-content-between.w-100>div"
            elem = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, title_css_selector))
            )

            #elem = driver.find_element(By.CSS_SELECTOR, title_css_selector)
            #print("App " + elem.text)
            if (codi in elem.text):
                isOk = True

        result = [isOk, ""]
    except TimeoutException as ex:
        result = [isOk, str(ex)]
    except:
        e = sys.exc_info()[0]
        result = [isOk, str(e)]
    finally:
        driver.quit()
        print("verify_apppage: "+str([codi]+result))
        return result


def write_csv(filename, fields, data):
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(fields)
        for rowdata in data:
            spamwriter.writerow(rowdata)


def rearrange_name(var):
    return "ok"


class Test(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "ok"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_proces(self):
        my_codi = "CLC0AP/093"
        my_proc = 0
        seu_result = verify_procediment(my_codi, my_proc)
        print("seu: "+str(seu_result))
        app_result = verify_apppage(my_codi, seu_result[1])
        print("app: "+str(app_result))

        self.assertEqual(True, seu_result[0])
        self.assertEqual(True, app_result[0])


"""
if __name__ == '__main__':
    unittest.main()
sys.exit("Quit script")

"""

# -- Init ----
start_time = time.time()
data = obtain_json(URL_json_cim)
result = {}

fieldnames = ['codi', 'idProcediment']
fieldnames.extend(['seu_codi_title_ok', 'seu_link_app', 'seu_err_msg'])
fieldnames.extend(['app_codi_ok', 'app_err_msg'])

keyCodi = 'Codi'
keyIdProcediment = 'idProcediment'

filtered_data = data#[78:]
data = filtered_data

print("Elements data: " + str(len(data)))

for index, item in enumerate(data):
    dictvalue = []
    codi = item[keyCodi]
    if (keyIdProcediment in item):
        idProcediment = item[keyIdProcediment]
    else:
        idProcediment = 0

    seu_result = verify_procediment(codi, idProcediment)
    app_result = verify_apppage(codi, seu_result[1])
    dictvalue.append(codi)
    dictvalue.append(idProcediment)
    dictvalue.extend(seu_result)
    dictvalue.extend(app_result)

    result[codi] = dictvalue
    print("....index: "+str(index)+" codi: "+codi+" "+str(dictvalue))

    """
    if(index>=1):
        print("---break: " + str(index) + " codi: " + codi)
        break #only test first element
    """

print("-----generating CSV")
headers = ['codi', 'idProcediment',
           'seu_codi_title_ok', 'seu_link_app', 'app_title_ok']
with open('result.csv', 'w', newline='') as csvfile:
    # , delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(headers)
    for key in result.keys():
        writer.writerow(result[key])

print("--- %s seconds ---" % (time.time()-start_time))
print("--------End: " + str(len(result)))

# -- End  ----


"""
codi = data[0]['Codi']
print(codi)
print("---json--")
result = verify_procediment(codi, idProcediment)
print(result)
print("---idProcediment-")
verify_convocatoriaapp(result[1])


filename="cimplaces.json"

print("---json-")
if os.path.exists(filename):
    os.remove(filename)
else:
    print("Can not delete the file as it doesn't exists")
download(URL_json_cim,filename)

filename="ajplaces.json"
if os.path.exists(filename):
    os.remove(filename)
else:
    print("Can not delete the file as it doesn't exists")
download(URL_json_ent,filename)

data = obtain_json(URL_json_ent)
codi = data[0]['Codi']
print(codi)
print("---json--")
result = verify_procediment(codi, idProcediment)
print(result)
print("---idProcediment-")
verify_convocatoriaapp(result[1])
print("---app-")

data = obtain_json(URL_json_ent)
print(data)
for item in data:
    print("Codi: {}, idProcediment: {}".format(item['Codi'],item['GrupSubgrup']))
    exit

with open('result.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
"""
