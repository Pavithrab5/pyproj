import calc
import unittest

class test_string(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,15),25)
        #self.assertEqual(calc.add(10.22,15.31),25.53)

if __name__ == '__main__':
    unittest.main()
