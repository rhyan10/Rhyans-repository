from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://friendorfollow.com/twitter/most-followers/').read()
soup = BeautifulSoup(r, "lxml")

#finds names of twitter accounts
def findtwittername():
    name = soup.find_all("h3")
    for textt in name:
        found_name = textt.text.strip()
        print found_name
        new= []
        for i in notags:
            if i.isalpha():
                new.append()
            else:
                pass
        return ''.join(new)

def findtwitterid():
    twitter_id = soup.find_all('a', attrs = {'class' :'tUSer'})
    for textt in twitter_id:
        found_twitter_id = textt.text.strip()
        new_id= []
        found_twitter_id
        for i in notags:
            if i.isalpha():
                new_id.append()
            else:
                pass

print findtwittername()
# print findtwitterid()



# print type(soup)
# print soup
