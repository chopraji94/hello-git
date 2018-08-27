"""Q.1- Name and handle the exception occured in the following program:
a=3
     if a<4:
        a=a/(a-3)
         print(a)"""

"""Exception here is the ZeroDivisionError ( Value Error )"""

a=3
if a<4:
    try:
        a=a/(a-3)
        print(a)
    except ZeroDivisionError as e:
        print('Exception:',e)

"""Q.2- Name and handle the exception occurred in the following program: 
l=[1,2,3] 
print(l[3]) """

"""Exception here is the IndexError ( Index Error )"""

l=[1,2,3]
try:
    print(l[3])
except IndexError as e:
    print('Exception:',e)


"""Q.3- What will be the output of the following code

  # Program to depict Raising Exception
     
    try:
        raise NameError("Hi there")  # Raise Error
    except NameError:
        print("An exception")
        raise  # To determine whether the exception was raised or not """

"This program will print ( An exception ) and then it will got Raise Error again"

"""Q.4- What will be the output of the following code: 

 # Function which returns a/b
    def AbyB(a , b):
        try:
            c = ((a+b) / (a-b))
        except ZeroDivisionError:
            print("a/b result in 0")
        else:
            print(c)
    
    # Driver program to test above function
    AbyB(2.0, 3.0)
    AbyB(3.0, 3.0)"""

"This program will print -5.0 whwn first function is called and will print a/b result in 0 when second function is called"

"""Q.5- Write a program to show and handle following exceptions: 
1. Import Error 
2. Value Error 
3. Index Error """

"1"
try:
    import pygame
except ModuleNotFoundError as e:
    print('Import Error: ',e)

"2."
try:
    int('dog')
except ValueError as e:
    print('Value Error: ',e)

"3."

str = 'abcd'
try:
    print(str[8])
except IndexError as e:
    print('Index Error: ',e)


