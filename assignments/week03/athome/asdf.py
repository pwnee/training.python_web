from bs4 import BeautifulSoup
import urllib2


response = urllib2.urlopen("http://www.j-archive.com/showgame.php?game_id=1337")
html = response.read()
f = open("jparty.html", "wb")
f.write(html)
f.close()
