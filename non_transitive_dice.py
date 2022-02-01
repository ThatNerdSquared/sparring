'''
ID: nathany5
LANG: PYTHON3
TASK: non_transitive_dice
'''

import sys
first_run_done = False
for line in sys.stdin:
    if not first_run_done:
        first_run_done = True
    else:
        input = list(line.rstrip().split(' '))
        is_possible = True
        diceA = input[:4]
        diceB = input[4:]
        counter = 0
        for num in diceA:
            if abs(int(diceA[counter]) - int(diceB[counter])) <= 1:
                is_possible = False
            counter += 1

        if is_possible:
            print('yes')
        else:
            print('no')
