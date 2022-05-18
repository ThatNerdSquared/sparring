import sys

cases = list(sys.stdin)
cases.pop(0)

for case in cases:
    caseint = int(case.strip())

    minimum = None
    max_amount_of_six = caseint // 6
    min_rem = caseint % 6
    if max_amount_of_six == 0:
        minimum = 1
    for item in range(max_amount_of_six):
        num_of_sixes = (caseint - (min_rem * item)) / 6
        if num_of_sixes.is_integer():
            if (caseint - 6 * num_of_sixes) % 4 == 0:
                minimum = num_of_sixes + ((caseint - 6 * num_of_sixes) / 4)
                break
    if minimum is None:
        print(-1)
        continue

    maximum = None
    max_amount_of_four = caseint // 4
    min_rem = caseint % 4
    if max_amount_of_four == 0:
        maximum = 1
    for item in range(max_amount_of_four):
        num_of_fours = (caseint - (min_rem * item)) / 4
        if num_of_fours.is_integer():
            if (caseint - 4 * num_of_fours) % 6 == 0:
                maximum = num_of_fours + ((caseint - 4 * num_of_fours) / 6)
                break
    if maximum is None:
        print(-1)
        continue

    print(int(minimum), int(maximum))
