#Lab 2
#PROBLEM 1
#a = 10
#b = 22
#print("The sum =", a+b)
#print("The difference =", a-b)
#print("The product =", a*b)
#print("The quotient =", a/b)
#print("The remainder =", a%b)
#print("The integer quotient =", a//b)
#print("The exponent =", a**b)

#PROBLEM 2
#x = 5
#x += 3
#print(x)

#PROBLEM 3
'''x = 20
y = 15
print("X is equal to Y:", x == y)
print("X is not equal to Y:", x != y)
print("X is Greater than Y:", x > y)
print("X is Less than Y:", x < y)
print("X is Greater than or equal to Y:", x >= y)
print("X is Less than or equal to Y:", x <= y)'''

#PROBLEM 4
'''x = 15
print(x > 13 and x < 20)''' #True (1 and 1=1)
'''x = 25
print(x > 23 or x < 24)'''#True ( 1 or 0 = 1)
'''x = 35
print(not(x > 33 and x < 40))''' #(not(1 and 1=1))=False

#PROBLEM 5,6,7,8
'''x = ["ahmed", "bashir"]
y = ["ahmed", "bashir"]
z = x
print(x is z)
print(x is y)
print(x == y)

print(x is not z)
print(x is not y)
print(x != y)'''# <> or !=

'''x = ["wasim", "lubaid", "shahroz", "usman", "faisal", "farhan"]
print("fail" not in x)'''# theyre saying that failis not in the list

#Lab 1
#PROBLEM 3
'''name = input("Enter your name: ")
age = int(input("Enter your age: "))

year = (100-age)+2020
print(name + " will be 100 years old in the year " + str(year))'''

#PROBLEM 4 Write a Python program to print the following
# string in a specific format
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#PROBLEM 5 date and time
'''import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))'''

#PROBLEM 6 area of circle
'''from math import pi
r = float(input("Input the radius of the circle : "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))'''

#PROBLEM 7
'''fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print("Hello  " + lname + " " + fname)'''

#problem 8
'''import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y,m))'''
