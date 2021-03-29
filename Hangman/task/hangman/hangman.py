import random


class Hangman:
    def __init__(self):
        self.words = ['java', 'python', 'kotlin', 'javascript']
        self.guessed = self.words[random.randint(0, len(self.words)-1)]
        self.guess = "-" * len(self.guessed)
        self.tries = 8
        self.guesses = list()

    def check(self, input_letter):
        if len(input_letter) != 1:
            print("You should input a single letter")
            return False
        elif input_letter in self.guesses:
            print("You've already guessed this letter")
            return False
        elif input_letter.isalpha() and input_letter.islower():
            return True
        else:
            print("Please enter a lowercase English letter")
            return False

    def game(self):
        while self.tries > 0:
            print()
            print(self.guess)
            print("Input a letter:", end='')
            word = input()
            if self.check(word):
                if word not in self.guessed:
                    print("That letter doesn't appear in the word")
                    self.tries -= 1
                elif word in self.guess:
                    print("You've already guessed this letter")
                elif word in self.guessed and word not in self.guess:
                    for i, char in enumerate(self.guessed):
                        if word == char:
                            self.guess = self.guess[0:i] + word+self.guess[i+1:]
                        if self.guess == self.guessed:
                            print("You guessed the word! ")
                            print("You survived!")
                            return
            self.guesses.append(word)
        print("You lost!")


def main():
    print("H A N G M A N\n")
    print('Type "play" to play a game,"exit" to quit:')
    entry = input()
    while True:
        if entry == "play".lower():
            hang = Hangman()
            hang.game()
            print('Type "play" to play a game,"exit" to quit:')
            entry = input()
        elif entry == "exit".lower():
            quit()
        else:
            print('Type "play" to play a game,"exit" to quit:')
            entry = input()

if __name__ == "__main__":
    main()