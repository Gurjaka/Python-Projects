import random
sia = ["Whispers in the Shadows", "The Enigma of Elmwood Manor", "Midnight Murmurs", "Echoes of Deception", "The Puzzle of the Missing Heirloom", "Fogbound Secrets", "The Cryptic Code", "Shattered Illusions", "The Case of the Vanishing Bride", "Secrets of the Forgotten Chamber", "The Edge of Darkness", "Deadly Pursuit", "Shadow Games", "Twisted Obsession", "The Abyss Beckons", "Rogue Agent", "Chaos Theory", "Blood Red Horizon", "The Last Stand", "Blackout", "Love in Bloom", "Hearts Entwined", "Forever Yours", "Sweet Serendipity", "Whispers of Passion", "The Perfect Match", "Romancing the Heart", "Eternal Flames", "Chasing Destiny", "A Love Beyond Time", "Galactic Odyssey", "Beyond the Event Horizon", "Chronicles of the Nebula", "The Quantum Paradox", "Echoes from Tomorrow", "Starsong", "The Android's Dilemma", "Temporal Rift", "The Last Frontier", "Alien Encounters", "Realm of Shadows", "The Dragon's Hoard", "Tales of Enchantment", "Echoes of Elvendom", "Sword of Destiny", "The Witching Hour", "Legends of Mythos", "The Crystal Key", "Wings of Magic", "Kingdoms Collide", "Echoes of Revolution", "The Silk Road Chronicles", "Secrets of the Renaissance", "A Tapestry of Time", "Memoirs of a Samurai", "The Tudor Enigma", "The Victorian Affair", "Shadows of Pompeii", "The Romanov Legacy", "Whispers of the Crusades", "Crimson Nightmares", "The Haunting of Hollow Hill", "Echoes of the Abyss", "Blood Moon Rising", "Whispers in the Dark", "The Demon Within", "Screams of the Forgotten", "Terror at Ravenwood Manor", "The Curse of Blackwood Forest", "Midnight Shadows", "The Art of Deception", "Shadows of Corruption", "The Silent Witness", "Echoes of Betrayal", "The Dark Side of Justice", "Deadly Alliances", "The Price of Vengeance", "Blood Money", "Crossfire", "Underworld Chronicles", "The Lost City of Atlantis", "Echoes of Exploration", "Journey to the Unknown", "Tales of the High Seas", "Quest for the Sacred Artifact", "The Forbidden Jungle", "Echoes of the Amazon", "Into the Wild", "The Treasure of El Dorado", "Secrets of the Sahara", "Echoes of Greatness: The Life of a Legend", "In the Footsteps of History", "A Journey Through Time: The Memoirs of a Pioneer", "The Courage Within: A True Story", "Voices of Resilience: A Biography", "Echoes of Triumph: A Life Well Lived", "The Path to Greatness: A Biography", "In Pursuit of Excellence: The Story of a Visionary", "Against All Odds: A Biography", "From Adversity to Achievement: The Story of a Survivor"]
filee = open("bases.txt", "w")

random_10 = []

for i in range(10):
    random_10.append(random.choice(sia))
    
filee.write(str(random_10))

filee.close()

filee = open("bases.txt", "a")

for i in range(5):
    filee.write(f"\n{random.randint(1,100)}")

filee.close()

filee = open("bases.txt", "r")
print(filee.read())
filee.close()