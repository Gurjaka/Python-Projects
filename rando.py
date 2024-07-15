import random
n = int(input("Num: "))
r = int(input("Range: "))
num = []
for i in range(n):
    num.append(random.randint(0,r))

n1 = random.randint(0,10)

print(num)
print(n1)

count = 0
while count < len(num):
    total = 0
    found = []
    for i in num[count:]:
        if total == n1:
            print(f"Found it! {found}")
            break
        else:
            total+=i
            found.append(i)
    if total == n1:
        break
    count +=1