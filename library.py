#gen ID like LIB00023 where firss section "LIB" last 5 chars is numer in five chars
reg_users= {}

genre = {"001":"Classics", "002":"Fantasy", "003":"Science Fiction", "004":"Self-help", "005":"Educational"}

publisher = {"001":"Penguin Random House", "002":"Simon & Schuster", "003":"HarperCollins", "004":"Macmillan Publishers"}

author = {"00001":"Jane Austen", "00002":"Harper Lee", "00003":"F.Scott Fitzgerald", "00004":"Mary Shelley", "00005":"George Orwell", "00006":"J.R.R. Tolkien",
"00007":"George R.R. Martin", "00008":"J.K. Rowling ", "00009":"C.S. Lewis", "00010":"TBrandon Sanderson"}

year = [1813, 1960, 1925, 1818, 1949, 1954, 1996, 1997, 1950, 2006, 1965, 1979, 1985, 1968, 1989, 1936, 2011, 1952, 2018, 2003, 2015, 1980, 2008, 2016]

last_id = 0
id_string ="LIB"
menu_items ={"1":"add user", "2":"find user", "x":"exit"}

def gen_id():
    global last_id
    if last_id==99999:
        return None
    else:
        new_id = id_string+f"{last_id+1:0>{5}}"
        last_id+=1
        return new_id

def menu_list():
    for key, value in menu_items.items():
        print(f"{key}) {value} ")
    
    # pass

def collect_info():
    name = input("Input name: ")
    surname = input("Input surname: ")
    phone_number = input("Input phone number: ")
    birthday = input("Input birthday (DD/MM/YY): ")
    piradi_nomeri = input("Input your P/N: ")
    paid_membership = input('Do you want to get the paid membership?\nif "yes" - you will be able to bring the book with you, outside the library\nif "no" - you can only read the book in the library.\nChoose your answer (yes or no): ').lower()
    user_info =[name,surname,phone_number,birthday,piradi_nomeri,paid_membership]
    return user_info

def find_user():
    identity = input("Input library id: ")
    for key, value in reg_users.items():
        if key == identity:
            return key,value


# main_code
while True:
    menu_list()
    menu_elem = input("enter menu elem : ")
    if menu_elem.lower() == "x":
        break
    elif menu_elem == "1":
        lib_id = gen_id()
        user_info = collect_info()
        reg_users.setdefault(lib_id,user_info)
    # for key, value in reg_users.items():
    #      print(key,value)
    elif menu_elem == "2":
        print(find_user())
        
