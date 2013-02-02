from cgi import parse_qs, escape
import re
import book_html
import bookdb

########################################################################################
#  NOTE: THE SET UP OF THIS SERVER IS BASED ON THE SIMPLE SERVER DESCRIBED ON THIS     #
#  WEBSITE: http://lucumr.pocoo.org/2007/5/21/getting-started-with-wsgi/ IN PARTICULAR #
#  THE FUNCTIONS not_found AND application REMAIN UNCHAGED.                            #
########################################################################################

def debug_mode(bool):
	if bool == True:
		server = 'localhost'
	else:
		server = '67.214.219.123' #VM on blueboxgrid
	return server

def index(environ, start_response):
    """This function will be mounted on "/" and display the list of books availabed."""
    start_response('200 OK', [('Content-Type', 'text/html')])
    titles = bookdb.BookDB().titles()
    html = book_html.make_html_for_main_page(titles)
    return [html]

def book_info(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	path = environ.get("PATH_INFO", "No path info found.")
	path = path[1:]
	database = bookdb.database
	html = book_html.make_html_for_book_info_page(path,database)
	return [html]

def image (environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	path = environ.get("PATH_INFO", "No path info found.")
	html = book_html.make_html_for_image(path)
	return [html]

def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']

# map urls to functions
urls = [
    (r'^$', index),
    (r'id[0-9]', book_info),
]

def application(environ, start_response):
    """
    The main WSGI application. Dispatch the current request to
    the functions from above and store the regular expression
    captures in the WSGI environment as  `myapp.url_args` so that
    the functions from above can access the url placeholders.

    If nothing matches call the `not_found` function.
    """
    path = environ.get('PATH_INFO', '').lstrip('/')    
    for regex, callback in urls:
        match = re.search(regex, path)        
        if match is not None:            
            environ['myapp.url_args'] = match.groups()            
            return callback(environ, start_response)
    return not_found(environ, start_response)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server_name = debug_mode(True)
    srv = make_server(server_name, 8080, application)
    srv.serve_forever()