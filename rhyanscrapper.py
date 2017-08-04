from bs4 import BeautifulSoup
import urllib2,lxml,urlparse,sys
r = urllib2.urlopen('http://friendorfollow.com/twitter/most-followers/').read()
soup = BeautifulSoup(r)
names = soup.find_all('h3')
#names = soup.find('<p class="mail"><a class="tUser")

for name in names:
    notags = name.text.strip()
    new= []
    for i in notags:
        if i.isalpha():
            new.append(i)
        else:
            pass


for link in soup.findAll('a', href=True):
    print(link.get('href'))
