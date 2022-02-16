import sys

input = [item.rstrip() for item in list(sys.stdin)]

inted = 0
must_together = []
must_apart = []
groups = []
violations = 0

for idx in range(len(input)):
    try:
        i = int(input[idx])
        inted += 1
        if inted == 1:
            for item_index in range(i):
                must_together.append(input[item_index+1].split(' '))
        elif inted == 2:
            for item_index in range(i):
                must_apart.append(input[item_index + idx + 1].split(' '))
        elif inted == 3:
            for group_index in range(i):
                groups.append(input[group_index + idx + 1].split(' '))
    except: pass

for item in must_together:
    where_first_guy = None
    where_second_guy = None
    for idx in range(len(groups)):
        if item[0] in groups[idx]:
            where_first_guy = idx
        if item[1] in groups[idx]:
            where_second_guy = idx
    if where_first_guy != where_second_guy:
        violations += 1

for item in must_apart:
    where_first_guy = None
    where_second_guy = None
    for idx in range(len(groups)):
        if item[0] in groups[idx]:
            where_first_guy = idx
        if item[1] in groups[idx]:
            where_second_guy = idx
    if where_first_guy == where_second_guy:
        violations += 1

print(violations)
