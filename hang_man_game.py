import random

# List of words to choose from
words = ["python", "hangman", "challenge", "programming", "algorithm"]

# Hangman figures for each incorrect attempt
hangman_figures = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def main():
    play_again = True
    
    while play_again:
        word = choose_word()
        guessed_letters = set()
        attempts_remaining = 6
        incorrect_guesses = set()
        
        print("Welcome to Hangman!")
        
        while attempts_remaining > 0:
            print(hangman_figures[6 - attempts_remaining])
            print(f"\nWord: {display_word(word, guessed_letters)}")
            print(f"Attempts remaining: {attempts_remaining}")
            print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
            
            guess = input("Guess a letter: ").lower()
            
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input. Please enter a single letter.")
                continue
            
            if guess in guessed_letters or guess in incorrect_guesses:
                print("You already guessed that letter.")
                continue
            
            if guess in word:
                guessed_letters.add(guess)
                if all(letter in guessed_letters for letter in word):
                    print(hangman_figures[6 - attempts_remaining])
                    print(f"\nCongratulations! You guessed the word: {word}")
                    break
            else:
                incorrect_guesses.add(guess)
                attempts_remaining -= 1
                print(f"Incorrect! The letter '{guess}' is not in the word.")
            
            if attempts_remaining == 0:
                print(hangman_figures[6])
                print(f"\nGame Over! The word was: {word}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower().startswith('y')

if __name__ == "__main__":
    main()
