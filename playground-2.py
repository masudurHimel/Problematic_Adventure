import random

# List of possible words for the game
word_list = ["apple", "banana", "cherry", "grape", "melon", "orange", "pear", "strawberry"]


def choose_word():
    return random.choice(word_list)


def evaluate_guess(secret_word, guess):
    # Check the guessed word against the secret word and provide feedback
    if len(guess) != len(secret_word):
        return "Invalid guess length. Guess again!"

    feedback = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback.append(guess[i].upper())  # Correct letter in correct position
        elif guess[i] in secret_word:
            feedback.append(guess[i])  # Correct letter in wrong position
        else:
            feedback.append("_")  # Incorrect letter
    return " ".join(feedback)


def play_wordle():
    secret_word = choose_word()
    attempts_left = 6

    print("Welcome to Wordle!")
    print("Try to guess the word in", attempts_left, "attempts.")

    while attempts_left > 0:
        guess = input("Enter your guess: ").lower()
        if guess == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break
        else:
            attempts_left -= 1
            feedback = evaluate_guess(secret_word, guess)
            print("Attempt(s) left:", attempts_left)
            print("Feedback:", feedback)

    if attempts_left == 0:
        print("Sorry, you're out of attempts. The secret word was:", secret_word)


if __name__ == "__main__":
    play_wordle()
