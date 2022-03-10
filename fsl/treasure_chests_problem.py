# A basic script to compute answers to problems involving n pirates walking down
# n chests, unlocking every nth
from math import sqrt

num_of_chests = int(input('What\'s the number of chests? '))

chests = [True] * num_of_chests

for idx in range(len(chests)):
    for i in range(len(chests)):
        if (i+1) % (idx+1) == 0:
            val = chests[i]
            chests[i] = not val

perfect_square_sum = 0
num_of_unlocked = 0

for idx in range(len(chests)):
    if chests[idx] == False:
        num_of_unlocked += 1
        perfect_square_sum += idx+1

print(f'Number of unlocked chests: {num_of_unlocked}')
print(f'Sum of chest numbers: {perfect_square_sum}')
