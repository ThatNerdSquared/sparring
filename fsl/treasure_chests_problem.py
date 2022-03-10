# A basic script to compute answers to problems involving n pirates walking down
# n chests, unlocking every nth
def optimized(num_of_chests):
    chests = [True] * num_of_chests

    for idx in range(len(chests)):
        for i in range(len(chests)):
            if (i+1) % (idx+1) == 0:
                chests[i] = not chests[i]

    unlocked = []
    for idx in range(len(chests)):
        if chests[idx] == False:
            unlocked.append(idx+1)
    return unlocked

n = int(input('How many chests are there? '))
unlocked = optimized(n)
print(f'Number of unlocked chests: {len(unlocked)}')
print(f'Sum of chest numbers: {sum(unlocked)}')
