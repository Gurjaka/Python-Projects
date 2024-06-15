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
    global sign
    game_table[y-1].pop(x-1)
    if turn % 2 == 0:
        game_table[y-1].insert(x-1, "X")
        sign = "X"
    else:
        game_table[y-1].insert(x-1, "O")
        sign = "O"

def win(x,y,sig):
        if turn < 5:
            pass
        else:
            if game_table[y-1][0]==game_table[y-1][1]==game_table[y-1][2]==sig :
                return True  
            elif game_table[0][x-1]==game_table[1][x-1]==game_table[2][x-1]==sig :
                return True
            elif ((x==2 or y==2) and (x!=y)) != True:
                if game_table[0][0]==game_table[1][1]==game_table[2][2]==sig or game_table[0][2]==game_table[1][1]==game_table[2][0]==sig:
                    return True   

while True:
    show_table()
    positions()
    change_positions()
    if win(x,y,sign):
        print("You win!")
        break