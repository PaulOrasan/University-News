import urllib.request, urllib.error
from bs4 import BeautifulSoup
from browser import Browser
from database import Database

# Preparing database for storing URLs
database = Database('links.sqlite')
database.createTable()

# Preparing browsers for opening links
Browser.initialize()

# Preparing target url for access
websiteURL = 'http://cs.ubbcluj.ro'
website = urllib.request.urlopen(websiteURL)
content = website.read()

# Parsing the html of the website, find all target tags of type h2
tags = BeautifulSoup(content,'html.parser')
newsTags = tags('h2')
#fsdhsfdhjk

# Process individual h2 tags
count = 0
for tag in newsTags:
    externalAddress = tag.find('a')
    link = externalAddress.get('href',None)
    if database.checkIfExists(link) == False:
        count += 1
        database.insertTable(link)
        Browser.openLink(link)

print ("Found ",count," new announcements!")
database.close()



