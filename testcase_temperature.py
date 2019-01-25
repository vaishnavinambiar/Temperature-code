import unittest
import datetime

year = int(raw_input("Enter the year "))
month = int(raw_input("Enter the month "))
day = int(raw_input("Enter the day "))
date = datetime.date(year, month, day)
temp=input("Enter the temperatures: ")
result=input("Type C for convert to Celsius and F for Fahrenheit:")
temperatures = []
my_dict = {}

class Test1(unittest.TestCase):
    def test_main(self):
        
        if result == 'C':
            convert= (9*temp+32*5)/5
            print("F= ", convert)
        elif result == 'F':
            convert = (5 * temp - 32 * 5) / 9
            print("C= ", convert)
            self.assertEqual(convert, 0.0)
            

    def test_user_input(temp):
         temperatures.append(temp)
         key = date
         my_dict.setdefault(date,[])
         my_dict[date].append(temperatures)
         my_dict[date] = [temperatures]
         return my_dict
         self.assertEqual(temp, 1.0)

      
    def test_min_max(self):
        min = 0
        max = 0
        self.assertEqual(min, 0)
        self.assertEqual(max, 0)
       
    def test_average(self):
        average = temp/1
        self.assertEqual(average, 1)
    
            
if __name__== '__main__':
    unittest.main()
