"""Q.1- Create a function to calculate the area of a sphere by taking radius from user."""

def area(radius):
    print("Area of sphere = ",4*3.14*(radius**2))

n = int(input("Enter the radius of sphere"))
area(n)

"""Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3]."""

def perfect(n1,n2):
    for i in range (n1,n2+1):
        s = 0
        for j in range(1,i):
            if i%j == 0:
                s = s + j
        if(i==s):
            print("Perfect number between given range is ",i)

perfect(1,101)

"""Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user."""

n = int(input("Enter the number to print the table"))

for i in range(1,11):
    print("%d x %d = %d"%(n,i,n*i)) 

"""Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion."""

def power(a,b):
    if(b == 1):
        return(a)
    if(b != -1):
        return(a*power(a,b-1))

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
print("Result : ",power(a,b))
