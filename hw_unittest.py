# import sys
import unittest
from lib.helloworld import Bob

# sys.path.append('../')

class TestSum(unittest.TestCase):
    def test_fizzbuzz(self):
        bob = Bob()
        result = bob.fizzbuzz(3)
        self.assertEqual(result, 'Fizz')

if __name__ == '__main__':
    unittest.main()
