"""Q.1- Take an input year from user and decide whether it is a leap year or not."""

year = int(input("Enter the year to check if it is leap year or not"))

if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("{0} is leap year".format(year))
        else:
            print("{0} is not leap year".format(year))
    else:
        print("{0} is leap year".format(year))
else:
    print("{0} is not leap year".format(year))

"""Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle. """

length = int(input("Enter the length"))
breadth = int(input("Enter the breadth"))

if(length == breadth):
    print("It is Square") #As square has both sides equal
else:
    print("It is Rectangel") #As Rectangle has both sides unequal

"""Q.3- Take the input age of 3 people and determine oldest and youngest among them."""

age1 = int(input("Enter the Age of first person"))
age2 = int(input("Enter the Age of second person"))
age3 = int(input("Enter the Age of third person"))

if(age1 > age2 & age1>age3):
    print("First person is younger")
elif(age2>age3):
    print("Second person is younger")
else:
    print("Third person is younger")

if(age1 < age2 and age1 < age3):
    print("First person is smaller")
elif(age2 < age3):
    print("Second person is smaller")
else:
    print("Third person is smaller")

"""Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

1. if employee is female, then she will work only in urban areas. 
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
4. And any other input of age should print "ERROR"."""

age = int(input("Enter the age of the employee"))
sex = input("Enter the sex of the employe ( M or F)")
mstatus = input("Enter the marital status ( Y or N )")

if(sex == 'F'):
    print("She can work only in urban areas.")
else:
    if(age > 20 and age < 40):
        print("He may work in anywhere")
    elif(age > 40 and age < 60):
        print("He will work in urban areas only.")
    else:
        print("ERROR.")

"""Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user."""

quantity = int(input("Enter the quantity purchased"))
sunit = 100
total = quantity*sunit

if(total > 1000):
    print(float((total)-((total*10)/100)))
else:
    print(total)

"""LOOPS"""

"""Q.1- Take 10 integers from user and print it on screen."""

l = []

print("Enter 10 integer value")
i=0
while(i < 10):
    n = int(input("Enter any number"))
    l.append(n)
    i=i+1

print("The 10 number entered are : ",l)

"""Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true. """

"""i = 0
    while(i < 100):
        print("Hi")"""

"""Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list."""

l1 = []
l2 = []

n = int(input("Enter the number of elements to enter in list 1 : "))

for i in range(0,n):
    num = int(input("Enter the number to put in list 1"))
    l2.append(num**2)

print("The square of elements of previous list : ",l2)

"""Q.4- From a list containing ints, strings and floats, make three lists to store them separately """

myList = [ 4,'a', 'b', 'c', 1, 'd', 3, 4.4, 2.2]
l = []
s = []
f = []

for i in myList:
    if isinstance(i,int):
        l.append(i);

for i in myList:
    if isinstance(i,str):
        s.append(i);

for i in myList:
    if isinstance(i,float):
        f.append(i);

print("Only Integer containing list: ",l)
print("Only String containing list: ",s)
print("Only Float containing list: ",f)

"""Q.5- Using range(1,101), make a list containing only prime numbers."""

l = []

for i in range(1,101):
    if i > 1:
        for j in range(2,i):
            if(i%j == 0):
                break
        else:
            l.append(i)

print("List of prime numbers",l)

""".6- Print the following patterns: 
* 
** 
*** 
****"""

for i in range(1,5):
    print('*'*i)

"""Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop."""

l1 = []
n = int(input("Enter the number of elements to enter in list l1"))

for i in range(0,n):
    ele = input("Enter the elements")
    l1.append(ele)

search = input("Enter the element to search in list l1")

f=0
for i in l1:
    if search == i:
        l1.remove(i)
        f=1

if(f == 0):
    print("Element not found list is : ",l1)
else:
    print("Element found and after deleting that element list is : ",l1)
    

