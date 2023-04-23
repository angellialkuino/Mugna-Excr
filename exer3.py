name1 = input('Enter Name 1: ')
name2 = input('Enter Name 2: ')

n1 = name1.replace(" ", "").lower()
n2 = name2.replace(" ", "").lower()

count = [0,0,0]
flame = ['','','']

for x in n1:
    if x in n2:
        count[0] += 1

for x in n2:
    if x in n1:
        count[1] += 1


count[2] = count[0]+count[1]

for i in range(3):
    if(count[i]%6==0):
        flame[i] = "SECRET"
    elif(count[i]%6==1):
        flame[i] = "FRIENDS"
    elif(count[i]%6==2):
        flame[i] = "LOVERS"
    elif(count[i]%6==3):
        flame[i] = "ACQUAINTANCES"
    elif(count[i]%6==4):
        flame[i] = "MARRIAGE"
    elif(count[i]%6==5):
        flame[i] = "ENEMIES"

print(f"Result for {name1} ==> {flame[0]}")
print(f"Result for {name2} ==> {flame[1]}")
print(f"FINAL RESULT ==> {flame[2]}")

