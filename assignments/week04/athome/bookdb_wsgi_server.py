#!/usr/bin/python
import datetime
import bookdb
import pprint
import cStringIO
from PIL import Image
body = """<html>
<head>
<title>WSGI Server - BookDB</title>
</head>
<body>
<h1><img border="0" src="/home/wilson/Projects/training.python_web/assignments/week04/athome/images/books.png" alt="Books" align="middle" width="170" height="151">The BookDB</h1>
%s
</body>
<footer>(c) WTB 2013</footer>
</html>"""

def application(environ, start_response):
	bookdb = get_titles()	
	titles = get_title_list(bookdb)
	ids = get_ids(bookdb)
	path = get_path_info(environ)
	#This is dangerous--users could just put in /id235rlkasjdf and it would try and make the HTML...
	#What's the best way to check to see that there is content that can be served for a given URL?
	#TODO: Figure the above out.  
	#TODO: Incorporate error handling.  404, 500, 501 etc.
	#Make a method to create the status and headers for a given request?
	if "id" in path:
		html = make_html_for_book_info_page(path,database)
	elif path == "/":
		html = make_html_for_main_page(titles, ids)
	elif "books.png" in path:
		#TODO: create method to return image--this is really quite ugly
		# Reference for displaying image via WSGI comes from this website.  Accessed 1/31/13: http://lost-theory.org/python/dynamicimg.html
		f = cStringIO.StringIO()
		img = Image.open("/home/wilson/Projects/training.python_web/assignments/week04/athome/images/books.png", "r")
		print img.size
		img.save(f, "PNG")		
		f.seek(0)
		response_body = f.read()
		print "rb:", response_body
		status = '200 OK'
		response_headers = [('Content-Type', 'image/png'),
						('Content-Length', str(len(response_body)))]
		start_response(status, response_headers)
		return [response_body]		
	else:
		html = "<h1>We couldn't find what you were looking for.   Sorry.</h1>"
	response_body = body % (html)
	status = '200 OK'
	response_headers = [('Content-Type', 'text/html'),
						('Content-Length', str(len(response_body)))]
	start_response(status, response_headers)
	return [response_body]		

def get_titles():
	return bookdb.BookDB().titles()


def get_title_list(bookdb):
	titles = []
	i = 0 
	while i < len(bookdb):
		titles.append(bookdb[i]['title'])
		i = i + 1
	return titles

def get_ids(bookdb):
	"""Returns the ids of all the books in an array."""
	ids = []
	i = 0
	while i < len(bookdb):
		ids.append(bookdb[i]['id'])
		i = i + 1
	return ids

def make_html_for_main_page(titles, ids):
	"""Takes in the titles of the books and the ids.  Returns an HTML link for
		each title in the list of titles. HTML is in this format:
			
		<a href=id1>Title of book id1</a><br>"
		
	"""
	html = ''
	i = 0
	for title in titles:
		html = "<a href={0}>{1}</a><br><br>".format(str(ids[i]) ,title) + html
		i = i + 1
	return html

def make_html_for_book_info_page(path, bookdb):
	"""Takes the path from the environ (essentially, whatever the user is requesting via HTTP) and returns
		HTML of the book details, along with a back button to go one step back in the user's history.
		HTML is in this format:
		
		<p>TITLE: title</p>
		<p>AUTHOR: author</p>
		<p>ISBN: isbn</p>
		<p>PUBLISHER: publisher</p>		
		
	"""
	#TODO: there is probably a better way of doing this--similar to how the HTML is created for the main page.  Maybe in a for loop
	book_id = path[1:]
	book_id = str(book_id)
	
	back_button_html = "<FORM><INPUT Type='"'button'"' VALUE='"'Back'"' onClick='"'history.go(-1);return true;'"'></FORM>"	
	html = "<p>TITLE: {0}</p>".format(database[book_id]["title"]) + "<p>AUTHOR: {0}</p>".format(database[book_id]["author"]) + "<p>ISBN: {0}</p>".format(database[book_id]["isbn"]) + "<p>PUBLISHER: {0}</p>".format(database[book_id]["publisher"]) + back_button_html
	return html


def get_path_info(environ):
	"""Returns the PATH_INFO from the request.  For a request to the website itself it returns "/".  If it can't find the key
		in the environ dictionary, it returns "Sorry, couldn't find that".	
	"""
	return environ.get("PATH_INFO", "Sorry, couldn't find that.")



#What's the right way of pulling in bookdb.py?  I feel kinda like this is cheating.
# Is the below the right way?
# from bookdb.py import * 
# 
database = {
	'id1' : {'title' : 'CherryPy Essentials: Rapid Python Web Application Development',
			 'isbn' : '978-1904811848',
			 'publisher' : 'Packt Publishing (March 31, 2007)',
			 'author' : 'Sylvain Hellegouarch',
		   },
	'id2' : {'title' : 'Python for Software Design: How to Think Like a Computer Scientist',
			 'isbn' : '978-0521725965',
			 'publisher' : 'Cambridge University Press; 1 edition (March 16, 2009)',
			 'author' : 'Allen B. Downey',
		   },
	'id3' : {'title' : 'Foundations of Python Network Programming',
			 'isbn' : '978-1430230038',
			 'publisher' : 'Apress; 2 edition (December 21, 2010)',
			 'author' : 'John Goerzen',
		   },
	'id4' : {'title' : 'Python Cookbook, Second Edition',
			 'isbn' : '978-0-596-00797-3',
			 'publisher' : 'O''Reilly Media',
			 'author' : 'Alex Martelli, Anna Ravenscroft, David Ascher',
		   },
	'id5' : {'title' : 'The Pragmatic Programmer: From Journeyman to Master',
			 'isbn' : '978-0201616224',
			 'publisher' : 'Addison-Wesley Professional (October 30, 1999)',
			 'author' : 'Andrew Hunt, David Thomas',
		   },
}

if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	srv = make_server('localhost', 8081, application)
	srv.serve_forever()

