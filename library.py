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

list_g = ["LIBZ.001.009.1992.006", "LIBZ.001.010.2012.007", "LIBZ.001.007.2004.010", "LIBZ.001.005.2012.005", "LIBZ.001.005.2004.007", "LIBZ.001.001.1970.006", "LIBZ.001.002.1970.004", "LIBZ.001.004.2015.005", "LIBZ.001.008.1999.001", "LIBZ.001.008.1970.009", "LIBZ.002.004.2009.005", "LIBZ.002.010.2015.008", "LIBZ.002.003.2009.010", "LIBZ.002.006.1970.003", "LIBZ.002.005.2001.010", "LIBZ.002.007.2004.001", "LIBZ.002.008.2012.010", "LIBZ.002.003.2004.006", "LIBZ.002.004.2012.003", "LIBZ.002.001.1970.004", "LIBZ.003.003.2009.004", "LIBZ.003.010.1985.007", "LIBZ.003.006.1985.003", "LIBZ.003.003.1970.010", "LIBZ.003.008.1985.008", "LIBZ.003.002.2015.001", "LIBZ.003.009.1970.007", "LIBZ.003.003.1970.010", "LIBZ.003.004.2015.009", "LIBZ.003.004.1992.010", "LIBZ.004.003.20011.004", "LIBZ.004.008.1970.006", "LIBZ.004.010.1992.004", "LIBZ.004.007.1999.010", "LIBZ.004.010.20011.001", "LIBZ.004.007.2009.002", "LIBZ.004.001.2001.010", "LIBZ.004.002.1992.009", "LIBZ.004.006.1970.009", "LIBZ.004.005.2009.009", "LIBZ.005.001.1992.006", "LIBZ.005.001.2001.009", "LIBZ.005.009.2012.007", "LIBZ.005.001.20011.010", "LIBZ.005.010.20011.010", "LIBZ.005.009.1999.010", "LIBZ.005.010.1999.005", "LIBZ.005.001.1970.007", "LIBZ.005.007.2004.005", "LIBZ.005.006.20011.001", "LIBZ.006.005.2004.006", "LIBZ.006.008.2004.002", "LIBZ.006.002.2015.003", "LIBZ.006.005.1992.002", "LIBZ.006.008.2004.002", "LIBZ.006.007.2001.008", "LIBZ.006.006.2009.001", "LIBZ.006.004.2012.001", "LIBZ.006.001.2004.001", "LIBZ.006.001.2015.002", "LIBZ.007.007.2004.006", "LIBZ.007.008.1999.001", "LIBZ.007.004.2015.001", "LIBZ.007.004.20011.004", "LIBZ.007.006.2009.009", "LIBZ.007.003.20011.003", "LIBZ.007.005.2004.004", "LIBZ.007.009.1992.007", "LIBZ.007.009.1999.003", "LIBZ.007.002.1992.001", "LIBZ.008.006.1999.008", "LIBZ.008.008.1985.004", "LIBZ.008.008.1985.008", "LIBZ.008.001.1985.007", "LIBZ.008.002.2004.001", "LIBZ.008.010.1970.007", "LIBZ.008.002.1999.007", "LIBZ.008.008.2012.004", "LIBZ.008.007.20011.002", "LIBZ.008.006.2012.004", "LIBZ.009.008.2004.005", "LIBZ.009.004.1999.001", "LIBZ.009.007.2009.001", "LIBZ.009.001.1999.004", "LIBZ.009.004.1985.002", "LIBZ.009.006.2012.008", "LIBZ.009.008.2004.005", "LIBZ.009.004.2001.003", "LIBZ.009.006.2015.008", "LIBZ.009.005.1992.007", "LIBZ.010.002.2004.010", "LIBZ.010.008.2015.004", "LIBZ.010.007.2004.002", "LIBZ.010.010.1985.001", "LIBZ.010.004.2012.002", "LIBZ.010.006.1999.001", "LIBZ.010.010.1999.008", "LIBZ.010.005.2009.003", "LIBZ.010.009.2015.009", "LIBZ.010.005.2004.001"]
list_b = ["Whispers in the Shadows", "The Enigma of Elmwood Manor", "Midnight Murmurs", "Echoes of Deception", "The Puzzle of the Missing Heirloom", "Fogbound Secrets", "The Cryptic Code", "Shattered Illusions", "The Case of the Vanishing Bride", "Secrets of the Forgotten Chamber", "The Edge of Darkness", "Deadly Pursuit", "Shadow Games", "Twisted Obsession", "The Abyss Beckons", "Rogue Agent", "Chaos Theory", "Blood Red Horizon", "The Last Stand", "Blackout", "Love in Bloom", "Hearts Entwined", "Forever Yours", "Sweet Serendipity", "Whispers of Passion", "The Perfect Match", "Romancing the Heart", "Eternal Flames", "Chasing Destiny", "A Love Beyond Time", "Galactic Odyssey", "Beyond the Event Horizon", "Chronicles of the Nebula", "The Quantum Paradox", "Echoes from Tomorrow", "Starsong", "The Android's Dilemma", "Temporal Rift", "The Last Frontier", "Alien Encounters", "Realm of Shadows", "The Dragon's Hoard", "Tales of Enchantment", "Echoes of Elvendom", "Sword of Destiny", "The Witching Hour", "Legends of Mythos", "The Crystal Key", "Wings of Magic", "Kingdoms Collide", "Echoes of Revolution", "The Silk Road Chronicles", "Secrets of the Renaissance", "A Tapestry of Time", "Memoirs of a Samurai", "The Tudor Enigma", "The Victorian Affair", "Shadows of Pompeii", "The Romanov Legacy", "Whispers of the Crusades", "Crimson Nightmares", "The Haunting of Hollow Hill", "Echoes of the Abyss", "Blood Moon Rising", "Whispers in the Dark", "The Demon Within", "Screams of the Forgotten", "Terror at Ravenwood Manor", "The Curse of Blackwood Forest", "Midnight Shadows", "The Art of Deception", "Shadows of Corruption", "The Silent Witness", "Echoes of Betrayal", "The Dark Side of Justice", "Deadly Alliances", "The Price of Vengeance", "Blood Money", "Crossfire", "Underworld Chronicles", "The Lost City of Atlantis", "Echoes of Exploration", "Journey to the Unknown", "Tales of the High Seas", "Quest for the Sacred Artifact", "The Forbidden Jungle", "Echoes of the Amazon", "Into the Wild", "The Treasure of El Dorado", "Secrets of the Sahara", "Echoes of Greatness: The Life of a Legend", "In the Footsteps of History", "A Journey Through Time: The Memoirs of a Pioneer", "The Courage Within: A True Story", "Voices of Resilience: A Biography", "Echoes of Triumph: A Life Well Lived", "The Path to Greatness: A Biography", "In Pursuit of Excellence: The Story of a Visionary", "Against All Odds: A Biography", "From Adversity to Achievement: The Story of a Survivor"]
book_base ={}
print(len(list_b))
print(len(list_g))
for i in range(len(list_g)):
    book_base.setdefault(list_g[i],list_b[i])
print(book_base)    

def gen_book_id():
    for i in genre.keys():
        for j in publisher.keys():
            for k in author.keys():
                for l in year:
                    print("Libz",i,j,k,l, sep=".")

def id_generator(x):
    import random
    x = random.choice(list(x.keys()))
    return x

def book_id_gen(y):
    while int(y) < 50:
        genre_id = id_generator(genre)
        publisher_id = id_generator(publisher)
        author_id = id_generator(author)
        import random
        year_id = random.choice(year)
        print(f"Libz{genre_id}.{publisher_id}.{author_id}.{year_id}")
        y += 1

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


book_id_gen(20)

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
        
