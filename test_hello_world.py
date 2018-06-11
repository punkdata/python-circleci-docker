import hello_world
import unittest

class TestHelloWorld(unittest.TestCase):

    def setUp (self):
        self.app = hello_world.app.test_client()
        self.app.testing = True
    
    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_messaged(self):
        response = self.app.get('/')
        self.assertEqual(response.data, 'Hello DockerCon 2018!')

if __name__ == '__main__':
    unittest.main()