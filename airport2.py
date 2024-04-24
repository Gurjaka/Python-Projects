import random
days = 30

while days > 0:
    parking_lot = 20
    print(days, "days left")
    workingparts = 8
    event = 0
    while event < workingparts:
        client = random.randint(0,1)
        if client == 1:
            print("we have", str(parking_lot), "lots")
            demand_lot = int(input("how many parking lots do you need? : "))
            while demand_lot > parking_lot:
                print("We don't have that much parking lots, please choose from range 1-20")
                demand_lot = int(input("how many parking lots do you need? : "))
            parking_lot = parking_lot - demand_lot
            if parking_lot == 0:
                print("we are out of parking lots")
                break
            elif parking_lot > 0:
                continue
        elif client == 0:
            print("No orders available")
        event = event + 1
    days -= 1