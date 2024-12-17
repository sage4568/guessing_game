import random

def animal_guessing_game():
    animals = ["elephant", "tiger", "lion", "giraffe", "zebra", "kangaroo", "penguin", "dolphin", "panda", "fox"]
    print("Welcome to the Animal Guessing Game!")
    print("I am thinking of an animal. Can you guess which one?")
    
    # Computer chooses a random animal
    animal_to_guess = random.choice(animals)
    attempts = 0
    
    while True:
        # Get user's guess
        guess = input("Your guess: ").strip().lower()
        attempts += 1
        
        if guess == animal_to_guess:
            print(f"Congratulations! You've guessed the animal in {attempts} attempts.")
            break
        elif guess not in animals:
            print("That animal is not in the list. Try again!")
        else:
            print("Wrong guess! Try again.")
    
    print("Thanks for playing!")

# Run the game
animal_guessing_game()