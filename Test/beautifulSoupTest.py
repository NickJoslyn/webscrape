from bs4 import BeautifulSoup
import urllib.request

url = "http://www.reddit.com/"
request = urllib.request.Request(url)
redditFile = urllib.request.urlopen(request)
redditHtml = redditFile.read()
redditFile.close()

soup = BeautifulSoup(redditHtml)
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))
