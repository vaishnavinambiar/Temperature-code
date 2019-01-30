import datetime

year = int(input("Enter the year "))
month = int(input("Enter the month "))
day = int(input("Enter the day "))
date = datetime.date(year, month, day)

my_dict = {}
temperatures = []
value = []

def get_user_temperature():
    
    for temp in range(3):
        temp=input("Enter the temperatures: ")
        result=input("Type C for convert to Celsius and F for Fahrenheit:")
        get_conversion(temp,result)
        value.append(temp)
    return value

def get_conversion(temp,result):
    """ This function converts temperature. """
    
    if result == 'C':
        convert= (9*temp+32*5)/5
        return ("F ="  , convert)
    elif result == 'F':
        convert = (5 * temp - 32 * 5) / 9
        return ("C= ", convert)

def get_user_date(temp):
    """ Intakes the user's temperature values and stores as in dict."""
    
    temperatures.append(temp)
    key = date
    my_dict.setdefault(date,[])
    my_dict[date].append(temperatures)
    my_dict[date] = [temperatures]
    return my_dict

def get_min_max(value):
    """ Displays the minimum and maximum temperature."""
    return ("maximum value is",max(value))
    return ("minimum value is",min(value))

def get_average(value):
    """ Finds the average."""
    return ("Average is",(value[0]+ value[1]+ value[2])/3)
    
if __name__ == "__main__":
    user_value=get_user_temperature()
    get_user_date(user_value)
    print my_dict
    get_min_max(value)
    print("maximum value is",max(value))
    print("minimum value is",min(value))
    print get_average(value)
        


    


              


        
        


      
                    
