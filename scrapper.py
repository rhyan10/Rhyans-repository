from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://friendorfollow.com/twitter/most-followers/').read()
soup = BeautifulSoup(r)
print type(soup)
print soup