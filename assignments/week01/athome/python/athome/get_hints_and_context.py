from get_jarchive import *
import urllib
import urllib2
from bs4 import BeautifulSoup


bs = get_jarchive_html(True)	
categories = get_categories(bs)
clue_dictionary = get_clues(bs, categories)



for x in range(1,7):
	for y in range (1,6):
		clue = "clue_J_" + str(x) + "_" + str(y)
		
		print clue_dictionary[clue]["correct_answer"]
		
#article = urllib.quote(article)
#

#opener = urllib2.build_opener()
#opener.addheaders = [('User-agent', 'Mozilla/5.0')] #wikipedia needs this

#resource = opener.open("http://en.wikipedia.org/wiki/" + article)
#data = resource.read()
#resource.close()
#soup = BeautifulSoup(data)
#print soup.find('div',id="bodyContent").p