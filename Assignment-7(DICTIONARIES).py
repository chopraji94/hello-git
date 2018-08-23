"""Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop."""

d={}
n = int(input("Enter how many elements to enter in dictionary"))

while (n > 0):
    index = input("Enter the key of the dictionary ")
    value = input("Enter the value corresponding to %s index "%(index))
    d[index] = value
    n=n-1

print("Dictionary is : ",d)

"""Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that dictionary for every subject. 
Hint: Use nested dictionary to store subjects marks."""

num = int(input("Enter the number of the students"))

student_info = {}
student_subject = {'s1','s2','s3'}

for i in range(0,num):
    student_name = input("Enter the student name ")
    student_info[student_name] = {}
    for j in student_subject:
        student_info[student_name][j] = int(input("Enter the marks in three subjects "))

name = input("Enter the name of the student ")
if name in student_info.keys():
    print("The marks scored by following student is : ",student_info[name].values())
else:
    print("Not found")
    
