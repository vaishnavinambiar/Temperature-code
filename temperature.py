import datetime

year = int(raw_input("Enter the year "))
month = int(raw_input("Enter the month "))
day = int(raw_input("Enter the day "))
date = datetime.date(year, month, day)
result=input("Type C for convert to Celsius and F for Fahrenheit:")
my_dict = {}
temperatures = []

def main():
    """ This function enters the temperatures and converts to farehneit or celcius. """
    for temp in range(3):
        temp=input("Enter the temperatures: ")
        temp=float(temp)
        get_user_temperature_input(temp)
        
        if result == 'C':
            convert= (9*temp+32*5)/5
            print("F= ", convert)
        elif result == 'F':
            convert = (5 * temp - 32 * 5) / 9
            print("C= ", convert)
        else:
            print("Please insert correct syntax")


def get_user_temperature_input(temp):
    """ Intakes the user's temperature values and stores as in dict."""
    
    temperatures.append(temp)
    key = date
    my_dict.setdefault(date,[])
    my_dict[date].append(temperatures)
    my_dict[date] = [temperatures]
    return my_dict


def get_min_max():
    """ Displays the minimum and maximum temperature from the user's dates as per the choice given."""
    
    choice_list=[1,2]
    for user_input in range(2):
        user_input=int(input("enter your choice:"))
        if(user_input==choice_list[0]):
            print max(my_dict[date][0])
        elif(user_input==choice_list[1]):
            print min(my_dict[date][0])

def get_average():
    average = (temperatures[0]+ temperatures[1]+temperatures[2])/3
    print ("Average is %d" %average)
    
        
if __name__ == "__main__":
    
    main()
    
    get_min_max()
    get_average()


    


              


        
        


      
                    
