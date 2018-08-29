"""Q.1- Write a Python program to read n lines of a file"""

with open('test.txt','r') as f:
    n=int(input("Enter The number of lines you want to enter"))
    for i in range(n):
        x=f.readline()
        print(x)

"""Q.2- Write a Python program to count the frequency of words in a file."""

f=open('alphacount.txt','r')
d=f.read()
words = d.split()
print(words)
l=[]
for i in words:
    if i not in l:
        l.append(i)
        p=words.count(i)
        print ('count of '+i+' = '+ str(p))

"""Q.3- Write a Python program to copy the contents of a file to another file"""

with open("test.txt") as f:
    with open("out.txt","w") as f1:
        for line in f:
            f1.write(line)

"""Q.4- Write a Python program to combine each line from first file with the corresponding line in second file."""

with open("test.txt") as f1,open("pyu28.txt") as f2,open("Combine.txt","w") as fout:
    for t1,t2 in zip(f1,f2):
        fout.write(t1+t2)

"""Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file."""

with open('Sort.txt','w') as f:
    for i in range(10):
        num = int(input("Enter any number"))
        f.write(' %d' % num)

with open('Sort.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        words = l.split()
    r = [int(i) for i in words]
    r.sort()
    str1 = ' '.join(str(e) for e in r)
    fout = open('Final.txt','w')
    fout.write(str1)
    fout.close()
