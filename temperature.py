import datetime

year = int(raw_input("Enter the year "))
month = int(raw_input("Enter the month "))
day = int(raw_input("Enter the day "))
date = datetime.date(year, month, day)
date_2 = datetime.date(year, month, day)
temp=input("Enter the temperatures: ")
result=input("Type C for convert to Celsius and F for Fahrenheit:")
my_dict = {}

def temperature():
    """ This function enters the temperatures and converts to farehneit or celcius. """
    for temp in range(3):
        temp=input("Enter the temperatures: ")
        temp=float(temp)
        
        if result == 'C':
            convert= (9*temp+32*5)/5
            print("F= ", convert)
        elif result == 'F':
            convert = (5 * temp - 32 * 5) / 9
            print("C= ", convert)
        else:
            print("Please insert correct syntax")

def user_input():
    """ Intakes the user's temperature values and stores as in dict."""
    temperatures = []
    temperatures.append(temp)
    my_dict = {}
    key = date
    my_dict.setdefault(date,[])
    my_dict[date].append(temperatures)
    my_dict[date] = [temperatures]
    return my_dict

def user_date():
    """ Intakes the user's date values."""
    year = int(raw_input("Enter the year "))
    month = int(raw_input("Enter the month "))
    day = int(raw_input("Enter the day "))
    date_2 = datetime.date(year, month, day)
    return date_2
        
        
def display_temp():
    """ Displays the minimum and maximum temperature from the user's dates as per the choice given."""
    choice_list=[1,2]
    for user_input in range(2):
        user_input=int(input("enter your choice:"))
        if(user_input==choice_list[0]):
            print max(my_dict[date][0])
        elif(user_input==choice_list[1]):
            print min(my_dict[date][0])

    
        

temperature()
user_input()
user_date()
display_temp()

    


              


        
        


      
                    
