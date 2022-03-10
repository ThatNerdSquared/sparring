# A basic script to compute answers to problems involving n pirates walking down
# n chests, unlocking every nth
import timeit

def optimized(num_of_chests):
    chests = [True] * num_of_chests

    for idx in range(len(chests)):
        chests = [not val if (i+1) % (idx+1) == 0 else val for i, val in enumerate(chests)]

    unlocked_chests = [idx+1 for idx, val in enumerate(chests) if val == False]
    return unlocked_chests

def prev(num_of_chests):
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

    return num_of_unlocked, perfect_square_sum
    # print(f'Number of unlocked chests: {num_of_unlocked}')
    # print(f'Sum of chest numbers: {perfect_square_sum}')

# n = int(input('How many chests are there? '))
# unlocked = optimized(n)
# print(f'Number of unlocked chests: {len(unlocked)}')
# print(f'Sum of chest numbers: {sum(unlocked)}')

print('Previous: ', timeit.timeit('prev(1000)', 'from __main__ import prev', number=1))
print('Optimized: ', timeit.timeit('optimized(1000)', 'from __main__ import optimized', number=1))
