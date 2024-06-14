import random

words = ["happy", "hungry", "tired", "water", "book", "big", "hot", "cold", "open", "close"]

warning = ["head", "body", "left hand", "right hand", "left foot", "right foot",]

display = [
"""
     _____
    |     |
    |      
    |
    |
    |
""",
"""
     _____
    |     |
    |     O
    |
    |
    |
""",
"""
     _____
    |     |
    |     O
    |     |
    |
    |
""",
"""
     _____
    |     |
    |     O
    |     |\\
    |
    |
""",
"""
     _____
    |     |
    |     O
    |    /|\\
    |
    |
""",
"""
     _____
    |     |
    |     O
    |    /|\\
    |      \\
    |
""",
"""
     _____
    |     |
    |     O
    |    /|\\
    |    / \\
    |
"""]

word_to_hang = random.choice(words)

word_output = "_" * len(word_to_hang)

attempts = -1
while True:
    print(f"{display[attempts+1]}\n {word_output} {5 - attempts} attempts left.\n")
    print(word_to_hang)
    
    
    if word_output == word_to_hang:
        print("You WIN")
        break        
    
    elif attempts == 5:
        print("You lose, you are out of attempts.")
        break

    guess = input("Guess a letter: ")


    if guess not in word_to_hang:
        attempts += 1
        print(f"warning: {warning[attempts]}.")
        continue

    else:
        for i in word_to_hang:
            if i == guess:
                word_output = word_output[:word_to_hang.find(i)] + guess + word_output[word_to_hang.find(i)+1:]
        continue



