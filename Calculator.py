First = int(input("Type first number: "))
Second = int(input("Type second number: "))
Operator = input("Choose operator from following: + ; -; *; /; ")
if Operator == "+": print("sum =", First + Second)
elif Operator == "-": print("sub =", First - Second)
elif Operator == "*": print("mul =", First * Second)
elif Operator == "/": print("div =", First / Second)

print(Operator)