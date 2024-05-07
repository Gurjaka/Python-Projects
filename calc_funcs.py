def Gamravleba(x,y):
    total = int(x) * int(y)
    return total
def Gayofa(x,y):
    total = int(x) / int(y)
    return total
def Mimateba(x,y):
    total = int(x) + int(y)
    return total
def Gamokleba(x,y):
    total = int(x) - int(y)
    return total

acts = [Gamravleba, Gayofa, Mimateba, Gamokleba]

x,y = input("Choose X: "), input("Choose Y: ")

operation = input("Choose operation from * ; / ; + ; - :")

# if operation == "*":
#     print(acts[0](x,y))
# elif operation == "/":
#     print(acts[1](x,y))
# elif operation == "+":
#     print(acts[2](x,y))
# elif operation == "-":
#     print(acts[3](x,y))



acts2 = {"*":Gamravleba,"/":Gayofa,"+":Mimateba,"-":Gamokleba}

if operation in acts2:
    print(acts2[operation](x,y))