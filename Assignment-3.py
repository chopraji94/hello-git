"""Q.1- Create a list with user defined inputs. """

n=int(input("Enter how many elements to  enter in the list"))
l = [] #initializing empty list so that we can insert or append value to that list

for i in range(0,n): #for loop is used to enter value again continuosly till the limit  of given number
    element = input("Enter the element")
    l.append(element) #Append function used to add element to the list

print("The list elements are as: ",l)


"""Q.2- Add the following list to above created list: [‘google’,’apple’,’facebook’,’microsoft’,’tesla’]"""

create =   ["google","apple","facebook","microsoft","tesla"]
l.extend(create)#Here extend is used to add the lists 
print("After adding the two list ",l)


"""Q.3- Count the number of time an object occurs in a list. """

n = [1,2,3,4,1,1]
print("The given list is: ",n) #Taking input of which number to find in list
num = int(input("Enter the number from list to find its occurence"))
print(n.count(num)) #Here Count function is being used to count th number of times an element is repeating

"""Q.4- create a list with numbers and sort it in ascending order. """

l_list = [1,4,5,2,7,8,9]
l_list.sort() #Sort function used to sort by default sorting is in ascending oreder
print(l_list)


"""Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item
from arrays A and B, in ascending order. [List]"""

A = [4,2,3,1]
B = [66,7,8,5]
A.sort() 
B.sort()
print("After sorting A ",A)
print("After sorting B ",B)
C = A+B # "+" operator is generally used to concatenate or merge to listor any element
C.sort()
print("After sorting the C array contains: ",C)

"""Q.6-Implement a stack and queue using lists."""

# stack using list
stack = ["Aman", "Ram", "Sham"] #In stack we follow LIFO(Last in first out) technique
stack.append("Raman")
stack.append("Rahul")
print("Stack is: ",stack)
print("Poped value: ",stack.pop()) #So according to LIFO at first pop() the element entered at last is poped out first
print("Stack is: ",stack)
print("Poped value: ",stack.pop())
print("Stack is: ",stack)

# queue using list
que = ["Aman", "Ram", "Sham"] #In Que we follow FIFO(First in first out) technique
que.append("Raman")
que.append("Rahul")
print("Que is: ",que)
front = 0
print("Poped value: ",stack.pop(front)) #So according to FIFO at first pop() the element entered at First is poped out first
print("Stack is: ",stack)
print("Poped value: ",stack.pop(front))
print("Stack is: ",stack)

"""OPTIONAL QUESTION
Q.1- Count even and odd numbers in that list."""

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2: #In this if condition it checks if number is odd and even and the if it give 0 the it goes to else other wise if as i have used not in if condition
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

