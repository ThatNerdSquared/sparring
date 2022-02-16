import sys

def search(positions):
    data['TOTAL_JUMPS'] = data['TOTAL_JUMPS'] + 1
    next_batch = []
    while positions != []:
        position = positions[0]
        positions.remove(position)

        new_positions = []
        data['already_checked'].append(position)

        # up_left
        new_positions.append([position[0] - 1, position[1] + 2])
        # up_right(position):
        new_positions.append([position[0] + 1, position[1] + 2])
        # down_left(position):
        new_positions.append([position[0] + 1, position[1] - 2])
        # down_right(position):
        new_positions.append([position[0] - 1, position[1] - 2])
        # left_up(position):
        new_positions.append([position[0] - 2, position[1] + 1])
        # left_down(position):
        new_positions.append([position[0] - 2, position[1] - 1])
        # right_up(position):
        new_positions.append([position[0] + 2, position[1] + 1])
        # right_down(position):
        new_positions.append([position[0] + 2, position[1] - 1])

        
        for square in new_positions:
            if square[0] > 0 and square[1] > 0 and square[0] < 9 and square[1] < 9:
                if square != data['end']:
                    if square not in data['already_checked']:
                        next_batch.append(square)
                else:
                    return print(data['TOTAL_JUMPS'])

        if positions == []:
            search(next_batch)

data = {}

index = 0

for line in sys.stdin:
    if index == 0:
        arr = line.split(' ')
        arr2 = []
        for item in arr:
           arr2.append(int(item.replace('\n', '')))
        data['start'] = arr2
    else:
        arr = line.split(' ')
        arr2 = []
        for item in arr:
           arr2.append(int(item.replace('\n', '')))
        data['end'] = arr2
    index = index + 1

data['TOTAL_JUMPS'] = 0

data['positions'] = [data['start']]
data['already_checked'] = []

search(data['positions'])
