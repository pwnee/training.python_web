from bs4 import BeautifulSoup
import urllib2


response = urllib2.urlopen("http://www.j-archive.com/showgame.php?game_id=1337")
html = response.read()
bs_html = BeautifulSoup(html)

#print bs_html

def get_categories(bs):
	#<td class="category_name">EUROPE</td></tr>
	allCategories = bs.findAll('td', {"class" : "category_name"})
	#TODO: Get Category Comments as well--might be helpful for the 
	#<td class="category_comments"></td></tr>
	#allCategoryComments = bs.findAll('td', {"class" : "category_comments"})
	categoriess = [] # List of All Categories
	for cat in allCategories:
		cats.append(cat.text)
	return categories

def get_clues(bs):
	allClues = bs.findAll(attrs={"class" : "clue"})
	for clue in allClues:
		if clue.find("div"):
			if clue.find(attrs={"class" : "clue_value"}) is not None:
				dollar_value = clue.find(attrs={"class" : "clue_value"}).text
			else:
				dollar_value = clue.find(attrs={"class": "clue_value_daily_double"}).text
			clue_text = clue.find(attrs={"class" : "clue_text"}).text		
			div = clue.find("div")	
			mouseover_js = div['onmouseover'].split(",",2)
			answer_soup = BeautifulSoup(mouseover_js[2]) 
			answer = answer_soup.find('em', {"class" : "correct_response"}).text
			round_dict = {}
			
			
			print dollar_value			
			print clue_text
			print answer
		else:
			print "NO CLUE HERE!"
			#clue_props = mouseover_js[1].split("_") #contains the unique ID of the clue for this specific game
	                                                #format: clue_["DJ"||"J"]_[Category(1-6]]_[Row(1-5)]
	            

#get_categories(bs_html)
get_clues(bs_html)














'''    if div:
        #Split the JS statement into it's arguments so we can extract the html from the final argument
        mouseover_js = div['onmouseover'].split(",",2)
        answer_soup = BeautifulSoup(mouseover_js[2]) #We need to go... deeper
        answer = answer_soup.find('em', {"class" : "correct_response"}).text
        
        clue_props = mouseover_js[1].split("_") #contains the unique ID of the clue for this specific game
                                                #format: clue_["DJ"||"J"]_[Category(1-6]]_[Row(1-5)]
                                                
        #Now to figure out the category
        cat = cats[int(clue_props[2])-1]

        #Are we in double jeopardy?
        dj = clue_props[1] == "DJ"

        #The class name for the dollar value varies if it's a daily double
        dollar_value = clue.find(attrs={"class" : re.compile('clue_value*')}).text
        clue_text = clue.find(attrs={"class" : "clue_text"}).text
        
        return {"answer" : answer, "category" : cat, "text" : clue_text, "dollar_value": dollar_value}
'''