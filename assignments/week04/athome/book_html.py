#!/usr/bin/python
import datetime
import bookdb

def make_html_for_main_page(titles):
	"""Takes in the titles of the books and the ids.  Returns an HTML link for
		each title in the list of titles. HTML is in this format:
			
		<a href=id1>Title of book id1</a><br>"
		
		Also provides a title and h1 in the HTML.
	"""
	html = """<html>
	<head>
	<title>WSGI Server - BookDB</title>
	</head>
	<h1>WSGI - Book Database</h1>
	<body>"""
	i = 0
	for title in titles:
		html = html + "<a href={0}>{1}</a><br><br>".format(str(titles[i]['id']) , titles[i]['title']) 
		i = i + 1
	return html + '</body>'

def make_html_for_book_info_page(path, database):
	"""Takes the path from the environ (essentially, whatever the user is requesting via HTTP) and returns
		HTML of the book details, along with a back button to go one step back in the user's history.
		HTML is in this format:
		
		<p>TITLE: title</p>
		<p>AUTHOR: author</p>
		<p>ISBN: isbn</p>
		<p>PUBLISHER: publisher</p>		
		
	"""

	back_button_html = "<FORM><INPUT Type='"'button'"' VALUE='"'Back'"' onClick='"'history.go(-1);return true;'"'></FORM>"	
	html = "<p>TITLE: {0}</p>".format(database[path]["title"]) + "<p>AUTHOR: {0}</p>".format(database[path]["author"]) + "<p>ISBN: {0}</p>".format(database[path]["isbn"]) + "<p>PUBLISHER: {0}</p>".format(database[path]["publisher"]) + back_button_html
	return html