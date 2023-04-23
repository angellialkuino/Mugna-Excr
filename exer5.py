
s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
s3 = input("Enter string 3: ")

arr = [s1,s2,s3]
    
with open('exer5.txt','a') as f:
    for s in arr:
        f.write(s + "\n")

with open('exer5.txt','r') as f:
    arr = [x.strip() for x in f.readlines()]
    arr.sort()

for i in arr:
    print(i)