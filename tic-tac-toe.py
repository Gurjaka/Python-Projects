game_table = [
    ["-","-","-"],
    ["-","-","-"],    
    ["-","-","-"]    
    ]

turn = 1

def show_table():
    for i in game_table:
        print(" ".join(i))

def positions():
    global x, y, turn
    turn += 1
    while True:
        x = error_check(input("\nInput X: "))
        y = error_check(input("\nInput Y: "))

        if game_table[y-1][x-1] != "-":
            print("That spot is already taken!")
            continue
        else:
            break
    
def error_check(pos):
    if pos in ["1","2","3"]:
        return  int(pos)
    else:
        print("Incorrect input")

def change_positions():
    game_table[y-1].pop(x-1)
    if turn % 2 == 0:
        game_table[y-1].insert(x-1, "X")
    else:
        game_table[y-1].insert(x-1, "O")

def win(x,y):
        if game_table[y-1][0]==game_table[y-1][1]==game_table[y-1][2]=="X" or game_table[y-1][0]==game_table[y-1][1]==game_table[y-1][2]=="O":
            return True  
        elif game_table[0][x-1]==game_table[1][x-1]==game_table[2][x-1]=="X" or game_table[0][x-1]==game_table[1][x-1]==game_table[2][x-1]=="O":
            return True
        elif ((x==2 or y==2) and (x!=y)) != True:
            if game_table[0][0]==game_table[1][1]==game_table[2][2]=="X" or game_table[0][0]==game_table[1][1]==game_table[2][2]=="O":
                return True
            

while True:
    show_table()
    positions()
    change_positions()
    if win(x,y):
        print("You win!")
        break