"""Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement"""

s1=input("enter first string : ")
s2=input("enter second string : ")
match s1==s2:
    case True:
        print("strings are identical")
    case False:
        print("Strings are NOT identical")    
