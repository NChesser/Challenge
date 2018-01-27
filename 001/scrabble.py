#Calculate the word with the highest Scrabble value

with open("dictionary.txt") as f:
    words = [word.strip() for word in f]

scrabble_values = {'-': 0, 'EAIONRTLSU': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4,
                    'K': 5, 'JX': 8, 'QZ': 10}

letter_values = {letter: score for letters, score in scrabble_values.items()
                              for letter in letters}


word_values = {word: sum([letter_values[c.upper()] for c in word]) for word in words}

max_word = max(word_values.keys(), key=(lambda k: word_values[k]))

print(max_word) # highest value word benzalphenylhydrazone - 56