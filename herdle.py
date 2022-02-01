'''
ID: nathany5
LANG: PYTHON3
TASK: herdle
'''

import sys

# Parsing input
answer_key = []
guess = []
for idx, line in enumerate(sys.stdin):
    if idx < 3:
        answer_key.extend(list(line.rstrip()))
    else:
        guess.extend(list(line.rstrip()))

green = 0
yellow = 0
done_letters = []

for letter in answer_key:
    if letter not in done_letters:
        done_letters.append(letter)
        correct_indices = list(filter(lambda x: answer_key[x] == letter, range(len(answer_key))))
        guessed_indices = list(filter(lambda x: guess[x] == letter, range(len(guess))))
        remaining_ci = correct_indices[:]
        remaining_gi = guessed_indices[:]

        for item in correct_indices:
            if item in guessed_indices:
                green += 1
                remaining_ci.remove(item)
                remaining_gi.remove(item)

        if len(remaining_gi) > len(remaining_ci):
            yellow += len(remaining_ci)
        else:
            yellow += len(remaining_gi)

print(green)
print(yellow)
