from bs4 import BeautifulSoup
import urllib2


#response = urllib2.urlopen("http://www.j-archive.com/showgame.php?game_id=1337")
#html = response.read()
f = open("jparty.html", "r")
data = f.read()
print data
bs_html = BeautifulSoup(data)
print bs_html


#print bs_html

def get_categories(bs):
	#<td class="category_name">EUROPE</td></tr>
	allCategories = bs.findAll('td', {"class" : "category_name"})
	#TODO: Get Category Comments as well--might be helpful for the 
	#<td class="category_comments"></td></tr>
	#allCategoryComments = bs.findAll('td', {"class" : "category_comments"})
	categories = [] # List of All Categories
	for cat in allCategories:
		cats.append(cat.text)
	return categories

def get_clues(bs):
	allClues = bs.findAll(attrs={"class" : "clue"})
	for clue in allClues:
		dollar_value = clue.find(attrs={"class" : "clue_value"}).text
		clue_text = clue.find(attrs={"class" : "clue_text"}).text		
		div = clue.find("div")	
		mouseover_js = div['onmouseover'].split(",",2)
		answer_soup = BeautifulSoup(mouseover_js[2]) 
		answer = answer_soup.find('em', {"class" : "correct_response"}).text
		round_dict = {}
		
		print clue_text
		print answer
		clue_props = mouseover_js[1].split("_") #contains the unique ID of the clue for this specific game
                                                #format: clue_["DJ"||"J"]_[Category(1-6]]_[Row(1-5)]
        print clue_props

#categories = get_categories(bs_html)
get_clues(bs_html)
