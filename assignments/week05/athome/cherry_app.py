import cherrypy
from jinja2 import Environment, FileSystemLoader
import sqlite3
from contextlib import closing


#config for db stuff
DATABASE = 'C:/tmp/cherrypy.db'
SECRET_KEY = 'development key'


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with 

env = Environment(loader=FileSystemLoader('templates'))

class Blog:    
    '''def index(self):   
        tmpl = env.get_template('index.html')
        return tmpl.render(salutation='Hello', target='World')        
    index.exposed = True'''
    def connect(thread_index): 
    # Create a connection and store it in the current thread 
        cherrypy.thread_data.db = MySQLdb.connect('host', 'user', 'password', 'dbname') 
    
    def index(self):
        c = cherrypy.thread_data.db.cursor() 
        c.execute('select count(*) from table') 
        res = c.fetchone() 
        c.close() 
        return "<html><body>Hello, you have %d records in your table</body></html>" % res[0]


if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    print "main"
    cherrypy.quickstart(Blog())
else:
    print "test"
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(HitCounter())

