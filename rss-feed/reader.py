#------------------------------------------------------------------------------
# Python version
#------------------------------------------------------------------------------
import sys
print(sys.version_info)

#------------------------------------------------------------------------------
# feedparser
#------------------------------------------------------------------------------
import feedparser
import webbrowser

feed = feedparser.parse("http://www.caib.es/eboibfront/indexrss.do?lang=ca")
print("{} [{}] \n{}\n".format(feed.feed.title,feed.feed.link,feed.feed.description))

# feed_title = feed['feed']['title']  # NOT VALID
feed_entries = feed.entries
print("Entries boib:", len(feed_entries))

for entry in feed.entries:

    print ("{}[{}]".format(entry.title, entry.link))
    print (" Published at {}".format(entry.published))
    #print ("Published by {}".format(entry.['dc:creator']))
    print(" Webpage {}".format(entry.guid))
    # print("catagory{}".format(article_tags))


#------------------------------------------------------------------------------
# url search
#------------------------------------------------------------------------------
# import urllib.request
# from xml.dom.minidom import parse, parseString

# with urllib.request.urlopen("http://www.caib.es/eboibfront/ca/2020/11201") as response:
#     html = response.read()

# print(html)


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.caib.es/eboibfront/ca/2020/11201")
driver.maximize_window()
time.sleep(5)
element = driver.find_element_by_class_name("primerosHijos")
print(element)
driver.close()