import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url:')
html = urllib.request.urlopen(url).read() #reads who file, not a for loop
soup = BeautifulSoup(html, 'html.parser') #takes file and makes it readable and organize for soup

# Retrieve all of the anchor tags
tags = soup('a') #<a>
for tag in tags:
  print(tag.get('href', None)) #only <a href> tags
