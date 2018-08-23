ex = True
while ex:
    name = input("Enter a student's name:" )
    f=0
    for ch in name:
        if ch.isspace():
            print("Enter a valid Name")
            f = 1
            break
        if ch.isdigit():
            print("Enter a valid Name")
            f = 1
            break
    if(f == 1):
        continue
    elif(f == 0):
        ex = False
        
ex = True
while ex:
    sex = input("Enter a student's sex:" )
    f=0
    for ch in sex:
        if ch.isspace():
            print("Enter a valid Student Sex")
            f = 1
            break
        if ch.isdigit():
            print("Enter a valid Student Sex")
            f = 1
            break
    if(f == 1):
        continue
    elif(f == 0):
        ex = False
sex = sex.upper()
if(sex == 'MALE'):
        print("Hello %s , sir"%(name))
elif(sex == 'FEMALE'):
        print("Hello %s , mam"%(name))
else:
        print("Invalid Input for sex")
ex = True
while ex:
    age = input("Enter a student's age:" )
    f=0
    for ch in age:
        if ch.isspace():
            print("Enter a valid student age")
            f = 0
            break
        if ch.isdigit():
            f = 1
            break
    if(f == 1):
        ex = False
    elif(f == 0):
        print("Input Age in numbers")
        continue

age  = int(age)
if(sex == 'MALE'):
    if(age > 20):
        print("You are  able  to enroll for python fundamental course ")
    else:
        print("You are below age criteria you can't enroll the course")
else:
       if(age > 19):
        print("You are available to enroll for core Java course")
       else:
            print("error will not displayed") 
