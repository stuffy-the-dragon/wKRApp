from wKRApp import app
import unittest 

class FlaskTestCase(unittest.TestCase):
	# Ensure that flask was set up correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# Ensure that the login page loads correctly
	def test_signin_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertTrue(b'Please sign in' in response.data)
		
   # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)

if __name__ == '__main__':
	unittest.main()

