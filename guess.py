# Simple guessing game

# Create a guessNumber function
def guessNumber():
    import random # Import random libraries
    import time # Import time libraries
    X = random.randint(1,100) # Define bounds for X
    tries = 4 # Define max number of attempts

    # Welcome new player, and introduce to game
    print("Lets play a guessing game, I will choose number between 1-100, and you have to guess it!\nYou will have 5 tries, each try you will get a hint.\nGood luck!")

    # Create a while loop
    while tries > -1:
        try:
            Guess = int(input("Guess the number: ")) # New variable to guess the number
            if Guess > 100 or Guess < 1: # Bounds checker more than 100
                print("Out of bounds, try again")
                #Guess = int(input("Guess the number: "))
                #tries = 5
            if Guess == X: # Check if guessed number is equal to X
                Play = input("You win, wanna play again? (yes/no): ") # You win screen
                if Play == "yes": # Add variables for a new game
                    X = random.randint(1,100)
                    Guess = int(input("Guess the number: "))
                    tries = 5
                    continue
                elif Play == "no": # Goodbye screen
                    print("See you later!")
                    time.sleep(3)
                    quit()
            elif Guess < X: # Check if guessed number is less than X
                print("You have " + str(tries) + " attempt(s) left, here is the hint: " + str(Guess) + " < X") # Give a hint to player

            elif Guess > X: # Check if guessed number is more than X 
                print("You have "+ str(tries) + " attempt(s) left, here is a hint: " + str(Guess) + " > X") # Give a hint to player
            
            tries = tries - 1 # Minus 1 attempt on each guess
            if tries == -1: # Check if there are no attempts left
                Play = input("You are out of guesses, want to play again? (yes/no): ") # Give re-play menu 
                if Play == "yes": # Add variables for a new game
                    X = random.randint(1,100)
                    Guess = int(input("Guess the number: "))
                    tries = 5
                    continue
                elif Play == "no": # Goodbye screen
                    print("See you soon!")
                    time.sleep(3)
                    quit()
        except ValueError:
            print("NaN, try again")
guessNumber()