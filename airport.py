def airport_parkingv1():
    try:
        import random
        days = 30
        cash = 0
        while days > 0:
            parking_lot = 100000
            print(days, "days left")
            working_hours = 9
            event = 0
            while event < working_hours:
                client = random.randint(0,1)
                if client == 1:
                    print("we have", parking_lot, "parking lots")
                    lot = int(input("How many parking lots do you need? : "))
                    while lot > parking_lot:
                        print("We don't have that much parking lots")
                        lot = int(input("How many parking lots do you need? : "))
                    if parking_lot == 0:
                        print("We are out of parking lots!")
                        break
                    car = 10  
                    price = int(lot) * car
                    parking = random.randint(1,100000)
                    ticket_code = "| |||| || | ||||| | ||"
                    border = 29
                    print("*" * border)
                    print("**\tParking Ticket\t   **")
                    print("**\tPrice:", str(price) + "\t   **")
                    print("**\tPark at:", str(parking) + "\t   **")
                    print("**\tTicket code:" + "\t   **")
                    print("**  " + ticket_code + " **")
                    print("*" * border)
                    parking_lot = parking_lot - lot
                    cash = cash + price
                elif client == 0:
                    print("No orders available")
                event = event + 1
            days = days -1
        print("Past month, we made", cash)
    except ValueError:
        print("NaN")

def airport_parkingv2():
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