"""Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday"""

user=input("enter what colour you like : ")
match 'yellow' in user:
    case True:
        print("monday")
match 'blue' in user:
    case True:
        print("tuesday")
match 'orange' in user:
    case True:
        print("wednesday")
match 'white' in user:
    case True:
        print("thursday")
match 'black' in user:
    case True:
        print("friday")
match 'red' in user:
    case True:
        print("saturday")
match 'yellow'or'blue'or'orange'or'white'or'black'or'red' not in user:
    case True:
         print("sunday")        
        
     
     

                                        

                
        
