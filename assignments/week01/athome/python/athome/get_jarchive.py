from bs4 import BeautifulSoup
import urllib2

def get_jarchive_html(debug):
	if debug == False:
		game_id = raw_input("Please type in the a game number you wish to get: ")
		url = "http://www.j-archive.com/showgame.php?game_id=" + str(game_id)	
		response =  urllib2.urlopen(url)
		#Added this in class 1/28
		if response.code == 200:
			html = response.read()
		else:
			raise Exception
		
		bs = BeautifulSoup(html)
		return bs_html
	elif debug == True:
		path = raw_input("Please type in the relative path to the html that you have on your local disk for J-Archive HTML: ")
		print "You entered, ", path
		f = open (str(path), "r")
		data = f.read()
		bs = BeautifulSoup(data)
		return bs

def get_categories(bs):
	''' Scrape the BeautifulSoup object that's passed in for the categories
		and return a list of categories: 
		- [0-5]  - Jeopardy Round Categories
		- [6-11] - Double Jeopardy Round Categories
		- [12]   - Final Jeopardy Category
	'''
	allCategories = bs.findAll('td', {"class" : "category_name"})
	#TODO: Get Category Comments as well--might be helpful for the 
	#<td class="category_comments"></td></tr>
	#allCategoryComments = bs.findAll('td', {"class" : "category_comments"})
	categories = [] # List of All Categories
	for cat in allCategories:
		categories.append(cat.text)
	return categories


def get_clues(bs, categories):
	"""Scrape the Beautiful Soup for all of the Jeopardy, Double Jeopary, and Final Jeopary clues.
	Returns a dictionary of clue dictionaries.  Each clue is in the following format with the exception of
	the fj_clue which does not have a row:
		"round" : round,
		"category" : category,
		"row" : row,
		"dollar_value": dollar_value,
		"clue_text" : clue_text,
		"correct_answer": answer,
		"daily_double" : dd		
	"""
	allClues = bs.findAll(attrs={"class" : "clue"})
	clue_dictionary = {}
	for clue in allClues:		
		if not clue.find("div"):
			#There isn't a div included, which means that this question was never answered. 
			#TODO: Fix logic to create a clue with the correct clue information, but a null clue
			#      text and answer because a user might ask for this clue and we don't have an actual clue.
			continue
		else:
			if not clue.find(attrs={"class" : "clue_value"}):
				dd = True
				dollar_value = clue.find(atts={"class" : "clue_value_daily_double"})
			else:
				dd = False
				dollar_value = clue.find(attrs={"class" : "clue_value"}).text
			clue_text = clue.find(attrs={"class" : "clue_text"}).text		
			div = clue.find("div")	
			mouseover_js = div['onmouseover'].split(",",2)
			answer_soup = BeautifulSoup(mouseover_js[2]) 
			answer = answer_soup.find('em', {"class" : "correct_response"}).text
			clue_props = mouseover_js[1].split("_") 
			#contains the unique ID of the clue for this specific game
            #format: clue_["DJ"||"J"]_[Category(1-6]]_[Row(1-5)]
			round = clue_props[1]
			category_number = clue_props[2]
			category = categories[int(category_number)]
			row = clue_props[3]
			clue_name = "clue_" + str(round) + "_" + str(category_number) + "_" + str(row)
			clue = {
				"round" : round,
				"category" : category,
				"row" : row,
				"dollar_value": dollar_value,
				"clue_text" : clue_text,
				"correct_answer": answer,
				"daily_double" : dd		   
					}
			
			clue_dictionary[clue_name] = clue
		fj_clue = get_final_jeopardy(bs, categories)
		clue_dictionary["clue_fj"] = fj_clue
	return clue_dictionary
    
def get_final_jeopardy(bs_html, categories):
	""" Grab the Final Jeopardy clue and return a clue dicionary to be added to the 
	clue dictionary.
	"""	
	category = categories[-1]
	clue_text = bs_html.find("td",{"id": "clue_FJ"}).text	
	finalj = bs_html.find("div", {"id": "final_jeopardy_round"})
	div = finalj.find("div")
	#TODO: Grab category_comments	
	#category_comments = finalj.find(atts={"class": "category_comments"}).text
	mouseover_js = div['onmouseover'].split(",",2)
	answer_soup = BeautifulSoup(mouseover_js[2]) 
	answer = answer_soup.find('em').text
	dollar_value = 0
	dd = False
	clue = {
		"round" : "FJ",
		"category" : category,		
		"dollar_value": dollar_value,
		"clue_text" : clue_text,
		"correct_answer": answer,
		"daily_double" : dd		   
		}
	return clue

#bs = get_jarchive_html(True)
#categories = get_categories(bs)
#clue_dictionary = get_clues(bs, categories)