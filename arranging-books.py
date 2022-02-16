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
for n in range(len(newput)):
    smallest_index = n
    for y in range(n+1, len(newput)):
        if newput[y] < newput[smallest_index]:
            smallest_index = y
            total_swaps += 1
    newput[smallest_index], newput[n] = newput[n], newput[smallest_index]

print(total_swaps)
