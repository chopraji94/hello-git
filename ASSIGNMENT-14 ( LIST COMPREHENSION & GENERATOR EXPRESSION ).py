"""Q.1- Write a python program to print the cube of each value of a list using list comprehension."""

l1 = [1,2,3,4]
x = [x**3 for x in l1]
print("After cube all elements in list")
print(x)

"""Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension."""

N = int(input("Enter the range upto which to find prime numbers"))
print("Prime number in range is")
x1 = [p for p in range(2,N) if 0 not in [p%d for d in range(2,p)]]
print(x1)

"""Q.3- Write the main differences between List Comprehension and Generator Expression."""

"""In terms of syntax, the only difference is that you use parenthesis instead of square brackets.
The main advantage of generator over a list is that it take much less memory."""

"""LAMBDA & MAP"""

"""Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression."""

Celsius = [39.2, 36.5, 37.3, 37.8]
print("List after conversion from celsius to farenhite")
m=list(map(lambda x:(x * 1.8) + 32,Celsius))
print(m)

"""Q.2- Apply an anonymous function to square all the elements of a list using map and lambda."""

l = [1,2,3,4]
print("After Squaring all the element in the list")
x = list(map(lambda x:x**2,l))
print(x)

"""FILTER & REDUCE"""

"""Q.1- Filter out all the primes from a list."""

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in range(2, 8): 
     nums = list(filter(lambda x: x == i or x % i and x > 1, nums))
print("After filtering all the elements from the list")
print(nums)

"""Q.2- Write a python program to multiply all the elements of a list using reduce."""

from functools import reduce
l1 = [1,2,3,4,5,6]
print("After multiplyong all the list element:")
r = reduce(lambda x, y: x*y,l1)
print(r)





