#1
def davaleba1():
    name = input("Name: ")
    for i in range(10):
        print(name)

#2
def davaleba2():
    name = input("Name: ")
    n = int(input("Input number: "))
    for i in range(n):
        print(name)

#3
def davaleba3():
    import random
    number = input("Number: ")
    n = random.randint(0,10)
    for i in range(n):
        print(number)

#4
def davaleba4():
    name = input("Name: ")
    for i in range(10):
        print(str(i)+")", name)

#5
def davaleba5():
    n = 0
    for i in range(10):
        n = n + i
    print(n)

#6
def davaleba6():
    n = 0
    for i in range(5,12):
        n = n + i
    print(n)

#7
def davaleba7():
    start = int(input("Choose first number: "))
    finish = int(input("Choose second number: "))
    n = 0
    for i in range(start,finish):
        n = n + i
    print(n)

#8
def davaleba8():
    import random
    first = random.randint(0,10)
    second = random.randint(10,20)
    n = 0
    for i in range(first,second):
        n = n + i
    print(n)

#9
def davaleba9():
    import random
    less = first = random.randint(0,100)
    more = second = random.randint(0,100)
    n = 0
    if first > second:
        less = second
        more = first    
    for i in range(less,more):
        n = n + i
    print(n)