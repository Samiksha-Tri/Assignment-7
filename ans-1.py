#Write a python script to display the number of days in a given month number.
n=int(input("enter month in numeric format : "))
match n:
    case 1:
        print("31 days")
    case 2:
        print("28 days")
    case 3:
        print("31 days")  
    case 4:
        print("30 days")      
    case 5:
        print("31 days")
    case 6:
        print("30 days") 
    case 7:
        print("31 days")
    case 8:
        print("31 days")
    case 9:
        print("30 days")               
    case 10:
        print("31 days")
    case 11:
        print("30 days")
    case 12:
        print("31 days") 
    case _:
        print("you entered wrong month number")               