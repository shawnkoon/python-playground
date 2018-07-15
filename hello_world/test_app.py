import unittest
from .app import get_print_string

class HelloWorldTest(unittest.TestCase):
    def test_get_print(self):
        name = ['Shawn', 'Jen']
        self.assertEqual(get_print_string(name[0]), f'Hello {name[0]}! This is Shawnkoon.')
        self.assertEqual(get_print_string(name[1]), f'Hello {name[1]}! This is Shawnkoon.')

if __name__ == '__main__':
    unittest.main()
