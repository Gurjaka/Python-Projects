data = input("Type combination of brackets: ")
pair = []


def data_checker1(data):
    global pair
    if len(data) % 2 == 1:
        return "This data is not balacned"
    if data == "":
        return "No data"

    for i in data:
        if i == "(":
            pair.append(i)
        elif i == ")" and pair == []:
            return "The data is not balanced"
        elif i == ")":
            pair.pop()
        
    if pair == []:
        return "This data is balanced"
    else:
        return "This data is not balanced"

#print(data_checker1(data))



def data_checker2(data):
    global pair
    if len(data) % 2 == 1:
        return "This data is not balanced."
    if data == "":
        return "No data."

    for i in data:
        if i in ("(", "[", "{"):
            pair.append(i)
        elif i in (")", "]", "}") and pair == []:
            return "The data is not balanced."
        elif i == ")" and pair[-1] == "(" or i == "]" and pair[-1] == "[" or i == "}" and pair[-1] == "{":
            pair.pop()
        
    if pair == []:
        return "This data is balanced."
    else:
        return "This data is not balanced."

print(data_checker2(data))
