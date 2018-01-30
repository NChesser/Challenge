import random
import csv
import os

from graphics import hang_graphics

HANG_GRAPHICS = list(hang_graphics())

class Hangman(object):
    def __init__(self, dictionary):
        self._word = [c.upper() for c in random.choice(dictionary)]
        self._player_word = self.setup_player()
        self._wrong_guesses = []
        self._hung = False

    def setup_player(self):
        return ['_' for _ in self._word]

    def prompt_player(self):
        print(self._word)
        print(self._player_word)
        print(str(len(self._wrong_guesses)) + " wrong guesses")

        player_input = input("Enter letter or guess word\n")

        if player_input.isalpha():
            if len(player_input) == 1 or len(player_input) == len(self._word):
                return self.check_guess(player_input.upper())
        else:
            print("You did not enter a letter, or a " + str(len(self._word)) + " letter word")
            return self.prompt_player()    

    def check_guess(self, guess):
        if guess in self._word:
            for i,v in enumerate(self._word):
                if guess == v:
                    self._player_word[i] = guess
        elif self._word == [c for c in guess]:
            self._player_word = self._word
        else:
            self._wrong_guesses.append(guess)     

        return self.is_solved()            
                
    def is_solved(self):
        print(HANG_GRAPHICS[len(self._wrong_guesses)])
        if len(self._wrong_guesses) == len(HANG_GRAPHICS)-1:
            self._hung = True
            return True        
        return self._player_word == self._word

    def game(self):
        print("Welcome to hangman")
        while not self.prompt_player():
            pass

        if self._hung:
            print("Game Over")
            print("The word was " + "".join(self._word))
        else:
            print("Congratz you guessed the word was " + "".join(self._word))
            self.save_score_to_csv()

    def save_score_to_csv(self):
        name = input("Please enter name for highscore\n")

        if not os.path.isfile('highscores.csv'):
            with open('highscores.csv', 'a', newline='') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(["Name", "Score"])

        with open('highscores.csv', 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([name, len(self._wrong_guesses)])

def load_dictionary(file):
    with open(file) as f:
        words = [word.strip() for word in f]
    return words

def get_highscores():
    
    with open('highscores.csv', newline='') as File:  
        reader = csv.reader(File)
        scores = [row for row in reader]
        scores.pop(0)

        return sorted(scores, key=lambda x: x[1])


if __name__ == "__main__":
    dictionary = load_dictionary('dictionary.txt')

    hangman = Hangman(dictionary)
    hangman.game()

    print()
    print("Highscores")

    for player in get_highscores():
        print(player[0] + " made " + str(player[1] + " wrong guesses"))

    
    
    
        





    