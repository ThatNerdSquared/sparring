input = [x.rstrip() for x in input()]

newput = []
for n in input:
    cases = {
        'L': 0,
        'M': 1,
        'S': 2,
    }
    newput.append(cases[n])

total_swaps = 0
for n in range(1, len(newput)):
    current = newput[n]
    x = n-1
    while x >= 0 and current < newput[x]:
        newput[x+1] = newput[x]
        x -= 1
        total_swaps += 1
    newput[x] = current

print(total_swaps)
