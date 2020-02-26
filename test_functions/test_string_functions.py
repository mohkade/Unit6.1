import unittest
from more_functions import string_functions

class MyTestCase(unittest.TestCase):

    def test_input(self):
        with self.subTest():
            self.assertEqual("python!python!python!", string_functions.output("pyton", 3))

if __name__ == '__main__':
    unittest.main()