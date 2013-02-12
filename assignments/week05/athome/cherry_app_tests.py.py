import cherrypy
import os
import unittest
import tempfile

class CherryTestCase(unittest.TestCase):    
    def setUp(self):
        db_fd = tempfile.mkstemp()
        self.db_fd, cherrypy.config['DATABASE'] = db_fd
        cherrypy.config['TESTING'] = True
        self.client = cherrypy.test_client()
        self.app = cherrypy

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(cherrypy.app.config['DATABASE'])

    def test_databse_setup(self):
        con = cherrypy.connect_db()
        cur = con.execute('PRAGMA tablet_info(entries);')
        rows = cur.fetchall()
        self.assertEquals(len(rows), 3)


if __name__ == '__main__':
    unittest.main()