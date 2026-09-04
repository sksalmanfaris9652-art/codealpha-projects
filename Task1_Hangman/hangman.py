
import random

words = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard"
]

MAX_INCORRECT_GUESSES = 6


def play_hangman():
    word = random.choice(words)

    guessed_letters = []
    
    incorrect_guesses = 0

    print("\n" + "=" * 40)
    print("        WELCOME TO HANGMAN")
    print("=" * 40)
    print("Guess the word one letter at a time.")
    print(f"You have {MAX_INCORRECT_GUESSES} incorrect guesses available.\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Guessed letters:", ", ".join(guessed_letters))
        print(
            f"Incorrect guesses: "
            f"{incorrect_guesses}/{MAX_INCORRECT_GUESSES}"
        )

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations!")
            print(f"You guessed the word: {word}")
            return

        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)


        if guess in word:
            print("✅ Correct guess!")
        else:
            incorrect_guesses += 1
            remaining = MAX_INCORRECT_GUESSES - incorrect_guesses
            print(f"❌ Wrong guess! {remaining} incorrect guesses remaining.")

    print("\n💀 Game Over!")
    print(f"The correct word was: {word}")


def main():
    while True:
        play_hangman()

        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if choice not in ["yes", "y"]:
            print("\nThanks for playing Hangman! 👋")
            break


if __name__ == "__main__":
    main()
