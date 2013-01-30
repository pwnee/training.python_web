from bs4 import BeautifulSoup
import urllib2
from get_jarchive import *
import urllib

bs = get_jarchive_html(True)    
categories = get_categories(bs)
clue_dictionary = get_clues(bs, categories)


def start_game():
    print "Welcome to Jeopardy with Hints. v0.1 \nIn this version of Jeopardy we supply you with hints pulled from various sources on the web.\nIf you need help just type "'"hintme"'" once you are at the answer prompt"
    name = raw_input("Great, now that that's out of the way, please input your name: ")
    print "Welcome to Jeopardy, ", name
    
#TODO Implement question picking
    
def ask_questions_for_category():
    
    print "In this version of Jeopardy, you don't get to select the clues.  You select the category and then answer all questions from lowest dollar amount to highest."
    print "In order to get started, please take a look at the categories for the Jeopardy round!"
    
    while len(categories) > 7: 
        print "Here are the categories:"
        for x in range (0,((len(categories) - 7))):
            print str(x) + ":" + categories[x]
        category = raw_input("Please type in the category number to select your category: ")
        category = int(category)
        print "Great! You selected: ", categories[category]
        #Remove category from list
        del categories[category]
        #Start with $100 
        print "Now we're going to get started with the $100 question for this category"
        #clue_name = "clue_" + str(round) + "_"+ str(category_number) + "_" + str(row)
        for x in range (1,6):
            clue = "clue_J_" + str(category+1) + "_" + str(x)
            #print clue
            print "The clue for {0} is:\n\n{1}".format(clue_dictionary[clue]["dollar_value"],clue_dictionary[clue]["clue_text"])
            answer = raw_input("\nPlease enter your answer or "'"hintme"'": ")
            if answer == "hintme":
                print "\nGetting hint information..."
                hint_text = get_hint_text(clue,clue_dictionary)
                display_hint_text(hint_text,clue_dictionary,clue)
            elif answer == clue_dictionary[clue]["correct_answer"]:
                print "\nYou are CORRECT!  Adding {0} to the bank!".format(clue_dictionary[clue]["dollar_value"])
            else:
                print "\nSorry, that was not an exact match to the question.\nI'll need to match input better in the future.\nThe correct answer is: {0}.".format(clue_dictionary[clue]["correct_answer"])

def get_hint_text(clue,clue_dictionary):
    correct_answer = clue_dictionary[clue]["correct_answer"]
    opener = urllib2.build_opener()
    url = "https://www.googleapis.com/freebase/v1/text/en/" + correct_answer.lower()
    print url
    resource = opener.open(url)
    data = resource.read()
    resource.close()
    return data
    
    '''correct_answer = clue_dictionary[clue]["correct_answer"]
    url_ending = urllib.quote(correct_answer)
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')] #wikipedia needs this
    resource = opener.open("http://en.wikipedia.org/wiki/" + url_ending)
    data = resource.read()
    resource.close()
    soup = BeautifulSoup(data)   
    return soup.find('div',id="bodyContent").p'''    

def display_hint_text(hint_text, clue_dictionary, clue):
    print "I'll show you word by word the first paragraph from Wikipedia.\nIf the correct answer is within the paragraph, you will see "'"CORRECTANSWER"'" output.\nHit "'"q"'" to stop and then enter your answer.  Press any key to continue to the next word."
    string = hint_text
    words = string.split(" ")
    x = len(words)
    i = 0
    while i < x:
        input = raw_input()
        if input == "q":
            print "Hope the hints helped!"
            break
        else:
            if clue_dictionary[clue]["correct_answer"] in words[i]:
                print "CORRECTANSWER"
            else:
                print words[i]
        i = i + 1

start_game()
ask_questions_for_category()

