"""Q.1- Reverse the whole list using list methods."""

l1 = [1,2,3,4]
print("The reversed list is : ",l1[::-1]) #l1[::-1] is used to print the list in reverse

"""Q.2- Print all the uppercase letters from a string."""

f=0
n = input("Enter the string to check if any uppercase letter exist")
for i in range(0,len(n)):
    if (n[i]>='A' and n[i]<='Z'):
        print("The Upper case letter in string is: ",n[i])
        f = 1
        
if(f == 0):
    print("No uppercase letter found")

"""Q.3- Split the user input on comma's and store the values in a list as integers."""

num = []
value = input("Input some values with commas")
list = value.split(",") #split(",")seprate each word after "," and put in " "
for n in list:
    num.append(int(n)) #here "ord()" this function is used to convert every charcter to int

print("After typecasting to int ",num)

"""Q.4- Check whether a string is palindromic or not."""

str1 = input("Enter the string to check wwether it is palandromic or not")

rev = str1[::-1]
if(rev == str1):
    print("Palindromic")
else:
    print("Not Palindromic")

"""Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy."""


import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.deepcopy(li1)
print ("The elements before deep copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")

print("\n")
li2[2][0] = 7

print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
    print (li2[i],end=" ")
 
print("\n")
print ("The original elements after deep copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")

"""In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object."""
"""In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object."""

