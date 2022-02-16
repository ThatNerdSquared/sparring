import sys

input = [item.rstrip() for item in list(sys.stdin)]
yard = {}
n = int(input[0])

for idx in range(n):
    yard[str(idx+1)] = [False] * n

y = int(input[1])
for idx in range(y):
    coords = [int(item) for item in input[idx+2].split(' ')]
    yard[str(coords[0])][coords[1]-1] = True

print(yard)

away = 0
for key in list(yard.keys()):
    item = yard[key].count(True)
    if item > away:
        away = item

sizes = n-away

square_sizes = list(range(sizes+1))
square_sizes.reverse()
square_sizes.pop()


for x in square_sizes:
    streak = 0
    global_frees = list(range(0, n))
    for item in list(yard.keys()):
        row = yard[item]
        free_indexes = []
        for idx in range(len(row)):
            if row[idx] == False:
                free_indexes.append(idx)
        valid = False
        consec = 0
        for idx in range(len(free_indexes)-1):
            if free_indexes[idx+1] - free_indexes[idx] > 1:
                consec = 0
            else:
                consec += 1
                if consec == x:
                    valid = True
        if valid:
            if len(free_indexes) != len(global_frees):
                for item in range(len(global_frees)):
                    if global_frees[item] not in free_indexes:
                        global_frees.pop(item)
                    if len(global_frees) >= x:
                        streak +=1
                        if streak == x:
                            print(streak)
                            exit()
        else:
            streak = 0
            global_frees = list(range(0, n))


