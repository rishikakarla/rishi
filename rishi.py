import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "watermelon"]  # List of words to choose from
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(secret_word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")
            if attempts == 0:
                print("Sorry, you're out of attempts! The word was:", secret_word)
                break
        else:
            print("Good guess!")
        
        word_display = display_word(secret_word, guessed_letters)
        print(word_display)

        if "_" not in word_display:
            print("Congratulations, you've guessed the word!")
            break

hangman()
