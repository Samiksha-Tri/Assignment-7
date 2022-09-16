"""Write a python program to check whether a given number is positive, negative or
zero using match case statement"""

n=int(input("enter a number : "))
match n>0:
    case True:
        print("positive")
    case False:
        print("negative")
    case _:
        print("zero")       

