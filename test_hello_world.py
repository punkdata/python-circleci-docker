import hello_world
import unittest

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = hello_world.app.test_client()
        self.app.testing = True
    
    def test_root_status(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code,200)

    def test_HelloWorld_value(self):
        result = self.app.get('/')
        self.assertEqual(result.data, hello_world.wrap_html('Hello DockerCon!'))

if __name__ == "__main__":
    unittest.main()