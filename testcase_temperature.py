import unittest
from temperature import *

class MyTest(unittest.TestCase):

    def test_get_user_temperature(self):
        self.value = get_user_temperature()
        self.assertEqual(value,[1, 2, 3])

    def test_get_user_date(self):
        self.my_dict = get_user_date(temp)
        self.assertEqual(my_dict, {datetime.date(2015, 5, 6): []})

    def test_get_min_max(self):
        maximum = 3
        self.assertNotEqual(maximum, 4)

    def test1_get_min_max(self):
        minumum = 1
        self.assertEqual(minimum, 1)
        
    def test_get_average(self):
        average = (1 + 2 + 3)/ 3
        self.assertEqual(average, 2)
        
        
if __name__ == '__main__':
    unittest.main()        
