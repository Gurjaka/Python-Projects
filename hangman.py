# word = "apple"
# word1 = ""


# for i in word:
#     if i == "p":
#         i = "5"
#     word1 += i

import random

words = ["happy", "hungry", "tired", "water", "book", "big", "hot", "cold", "open", "close"]

w1 = "head"
w2 = "body"
w3 = "left hand"
w4 = "right hand"
w5 = "left foot"
w6 = "right foot"

word_to_hang = random.choice(words)

word_output = "_" * len(word_to_hang)

guess_list = []

attempts = 0
while attempts < 6:
    print("\n" + word_output, 6 - attempts, "attempts left.\n")
    guess = input("Guess a letter: ")
    
    if word_output == word_to_hang:
        print("You WIN")
        break        
    
    elif attempts == 6:
        print("You lose, you are out of attempts.")

    else:
        for i in word_to_hang:
            if i == guess:
                word_output = word_output[:word_to_hang.find(i)] + guess + word_output[word_to_hang.find(i)+1:]
    attempts += 1

    