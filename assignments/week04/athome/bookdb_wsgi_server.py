#!/usr/bin/python
import datetime
import bookdb
import pprint
body = """<html>
<head>
<title>WSGI Server - BookDB</title>
</head>
<body>
<h1>The BookDB</h1>

%s

</body>
</html>"""

'''
def application(environ, start_response):
    bookdb =  get_bookdb()
    print bookdb
    titles = get_title_list(bookdb)
    ids = get_ids(bookdb)
    if get_path_info(environ) == "/":
        html = make_html_for_main_page(titles, ids)
        response_body = body % (html)
        status = '200 OK'
        response_headers = [('Content-Type', 'text/html'),
                            ('Content-Length', str(len(response_body)))]
        start_response(status, response_headers)
        #pp = pprint.PrettyPrinter()
        #pp.pprint(environ)
        #print environ    
        return [response_body]
    elif "id" in get_path_info(environ):
        #this means the user is looking for a book...
        path = get_path_info(environ)
        print "THE PATH: ", path
        return make_html_for_book_info_page(path, database)
'''

def application(environ, start_response):
    bookdb =  get_bookdb()    
    titles = get_title_list(bookdb)
    ids = get_ids(bookdb)
    if get_path_info(environ) == "/":
        html = make_html_for_main_page(titles, ids)
        response_body = body % (html)
        status = '200 OK'
        response_headers = [('Content-Type', 'text/html'),
                            ('Content-Length', str(len(response_body)))]
        start_response(status, response_headers)
        #pp = pprint.PrettyPrinter()
        #pp.pprint(environ)
        #print environ    
        return [response_body]

def get_bookdb():
    return bookdb.BookDB().titles()

def get_title_list(bookdb):
    titles = []
    i = 0 
    while i < len(bookdb):
        titles.append(bookdb[i]['title'])
        i = i + 1
    return titles

def get_ids(bookdb):
    ids = []
    i = 0
    while i < len(bookdb):
        ids.append(bookdb[i]['id'])
        i = i + 1
    return ids

def make_html_for_main_page(titles, ids):
    html = ''
    i = 0
    for title in titles:
        html = "<a href={0}>{1}</a><br>".format(str(ids[i]) ,title) + html
        i = i + 1
    return html

def make_html_for_book_info_page(path, bookdb):
    book_id = path[1:]
    book_id = str(book_id)
    print "book_id: ", book_id
    print "DB:" , database[book_id]["title"]
    #for entries in database[book_id]:
    html = "<li>TITLE: {0}</li>".format(database[book_id]["title"])
    print html
    return html
    #return "Here is the book information for {0} : {1}".format(id,)

#bookdb = get_bookdb()
#print make_html_for_book_info_page(bookdb, "id3")


def get_path_info(environ):
    return environ.get("PATH_INFO", "Sorry, couldn't find that.")




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
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()

