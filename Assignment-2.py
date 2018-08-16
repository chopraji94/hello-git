"""Q.1- Print anything you want on screen."""

print('Hello World') #String always writeen in double or single quotes
print(1) #The numeric value can be printed with or without double or single quotes


"""Q.2- Join two strings using '+'.E.g.-"Acad"+"View”"""

a = "Acad" #"Acad" is being assigned to variable a which is of string type made at runtime or dynamically
b = "View" #"View is being assigned to b which is of string type made at runtime or dynamically
c = a+b    #"+" operator helps to concatenate two strings but it is possible only when both side have same datatype variables
print(c)


"""Q.3- Take the input of 3 variables x, y and z . Print their values on screen. """

a = input("Enter the 1 input") #This take input of both as numbers and alphabets but inform of string
b = input("Enter the 2 input")
c = int(input("Enter the third input")) #The int type cast will take input only numericals as they are of base 10 not the strings

print("1 input ",a)
print("2 input ",b)
print("3 input ",c)


"""Q.4- Print “Let’s get started” on screen."""

print('“Let’s get started”') #A string print line can't contain same quote in one line so we have to make use of different quotes


"""Q.5- Print the following values using placeholders. s=”Acadview” course=”Python” fees=5000"""

s = "Acadview"
course = "Python"
fees = 5000
print ("%s %s %s"%(s,course,fees)) #A placeholder make it easy to insert the value in a line just by using specific placeholder


"""Q.6- Let’s do some interesting exercise: name=”Tony Stark” salary=1000000 print(‘%s’’%d’)%(____ ,____)"""

name="Tony Stark"
salary=1000000
print('%s"%d'%(name,salary)) ##As in given question the print statement was not containing 2 brackets so as to close statement in print function so after puting the brackets it prints th statement
