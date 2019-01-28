import unittest
from temperature import *


temp=input("Enter the temperatures")
class MyTestCase(unittest.TestCase):
    def test_main(self):
        self.temp = main()
        self.assertEqual(temp,32)
    def test_get_user_temperature_input(self):
        self.my_dict = get_user_temperature_input(temp)
        self.assertEqual(my_dict, {datetime.date(2015, 5, 6): [[32]]})
    def test_get_min_max(self):
        self.choice_list[0]= get_min_max()
        self.assertEqual(max({datetime.date(2015, 5, 6): [[0]]}, 32))
    def test_get_average(self):
        self.average= average()
        self.assertEqual(average, 32)


       

        
    
if __name__ == '__main__':
    unittest.main()        
    
