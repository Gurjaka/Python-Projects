roomX = int(input("Input room width: "))
roomY = int(input("Input room length: "))
roomZ = int(input("Input room height: "))

print("\nStoring the information. \nWidth = " + str(roomX) + "\nLength = " + str(roomY) + "\nHeight = " + str(roomZ))

Cycle = input("\nDo you want to procceed to selection menu? (yes/no): ")

while(Cycle != "yes"):
    if Cycle != "no":
        print("\nIncorrect option")
    if Cycle == "no":
        Cycle = input("\nAre you sure? (yes/no): ")
        if Cycle == "no":
            Cycle = input("\nDo you want to procceed to selection menu? (yes/no): ")
        elif Cycle == "yes":
            quit()
    elif Cycle == "yes":
        break

while Cycle == "yes":
    print("\nOperation menu: \n1) P of the area \n2) Area \n3) Volume")

    operation = input("\nChoose the operation: ")

    if operation == "1": 
        total = roomX * 2 + roomY * 2
    elif operation == "2": 
        total = (roomX * roomZ * 2) + (roomY * roomZ * 2)
    elif operation == "3": 
        total = roomX * roomY * roomZ
    else: total = "\nIncorrect option"

    print("\nThe operation = " + str(total))

    Cycle = input("\nDo you want to choose another operation? (yes/no): ")
    
    if Cycle == "yes":
        continue

    while Cycle == "no":
        Cycle = input("\nAre you sure? (yes/no): ")
        if Cycle == "no":
            Cycle = input("\nDo you want to choose another operation? (yes/no): ")
        elif Cycle == "yes":
            quit()
    
    if Cycle != "yes" or Cycle != "no":
        print("\nIncorrect option")
    Cycle = input("\nDo you want to choose another operation? (yes/no): ")