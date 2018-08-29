"""Q.1- Write a Python program to read n lines of a file"""

f = open('test.txt','r')
data = f.read()
print(data)
f.close()

"""Q.2- Write a Python program to count the frequency of words in a file."""

count = 0

with open("alphacount.txt", 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isalpha()):
                   count = count+1

print("The number of alpahabets in given file is",count)

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
