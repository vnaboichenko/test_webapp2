import unittest
import webapp2
from web import HelloWebapp2
from web import app


class TestHandlers(unittest.TestCase):
   def test_with_headers(self):
       headers = {'ACCEPT': 'test'}
       request = webapp2.Request.blank('/', headers=headers)
       response = request.get_response(app)
       self.assertEqual(response.status_int, 200)
       self.assertEqual(response.body, "{'message': 'Good Morning'}")
   def test_with_no_headers(self):
       headers = {}
       request = webapp2.Request.blank('/', headers=headers)
       response = request.get_response(app)
       self.assertEqual(response.status_int, 200)
       self.assertEqual(response.body, "<p>Hello, World</p>")


loader = unittest.TestLoader()
suite = loader.loadTestsFromTestCase(TestHandlers)
runner = unittest.TextTestRunner()
runner.run(suite)



