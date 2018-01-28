# Scrabble game

import random

with open("dictionary.txt") as f:
    words = [word.strip() for word in f]

scrabble_values = {'-': 0, 'EAIONRTLSU': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4,
                    'K': 5, 'JX': 8, 'QZ': 10}

letter_values = {letter: score for letters, score in scrabble_values.items()
                              for letter in letters}

word_values = {word.upper(): sum([letter_values[c.upper()] for c in word]) for word in words}

# Generate most valuable 7 letter word

letter_amounts = {'E': 12, 'AI': 9, 'O': 8, 'NTR': 6, 'LSUD': 4, 'G': 3,
                    'BCMPFHVWY': 2, 'KJXQZ': 1}

# create letters
letters = [letter for k,v in letter_amounts.items() for c in range(v) for letter in k]

# generate player hand
hand = [random.choice(letters) for letter in range(7)]

print(hand)

# work out all the possible words that can be created, then select highest value

import itertools

# get all possible hand permutations
def all_permutations(iterable):
    perms = []
    for i in range(len(iterable)):
        perms += itertools.permutations(iterable, i)
    
    return map("".join, perms)   

all_perms = all_permutations(hand)

# store words that are in dictionary and in hand
hand_words = {word: word_values[word] for word in all_perms if word in word_values.keys()}

# display all words, then print max
print(hand_words)
max_word = max(hand_words, key=(lambda k: hand_words[k]))
print(max_word + " - " + str(hand_words[max_word]))