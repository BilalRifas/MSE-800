import random
import string


class WordGuessGame:
    def __init__(self, max_lives=6):
        self.words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]
        self.max_lives = max_lives
        self.secret_word = self.get_random_word()
        self.blanks = self.make_blanks()
        self.lives = max_lives
        self.used_letters = set()

    def get_random_word(self):
        return random.choice(self.words)

    def make_blanks(self):
        return ["_" for _ in self.secret_word]

    def prompt_for_letter(self):
        while True:
            guess = input("Guess a letter: ").strip().lower()

            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print("→ Please enter a single A-Z letter.")
                continue

            if guess in self.used_letters:
                print("→ You already tried that letter.")
                continue

            return guess

    def reveal_letters(self, letter):
        found_any = False

        for i, ch in enumerate(self.secret_word):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True

        return found_any

    def all_blanks_filled(self):
        return "_" not in self.blanks

    def play(self):
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret_word)} letters.")
        print(" ".join(self.blanks))

        while True:
            guess = self.prompt_for_letter()
            self.used_letters.add(guess)

            if self.reveal_letters(guess):
                print("\nWell done! You found a letter.")
                print(" ".join(self.blanks))

                if self.all_blanks_filled():
                    print("\nCongratulations! You guessed the word!")
                    print(f"Word: {self.secret_word}")
                    print("GAME OVER")
                    break

            else:
                self.lives -= 1
                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                print(" ".join(self.blanks))

                if self.lives <= 0:
                    print("\nOut of lives! Sad story!")
                    print(f"The word was: {self.secret_word}")
                    print("GAME OVER")
                    break


def main():
    game = WordGuessGame()  # Object creation
    game.play()


if __name__ == "__main__":
    main()