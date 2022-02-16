import sys

input = list(sys.stdin)
total = int(input[0].rstrip())
input.pop(0)
newput = [int(item.rstrip()) for item in input]

players = []
total_stars = 0
for idx in range(len(newput)):
    if idx % 2 == 0:
        players.append([newput[idx], newput[idx+1]])

for player in players:
    stars = player[0] * 5 - player[1] * 3
    if stars > 40:
        total_stars += 1

if total_stars == total:
    print("".join([str(total_stars), '+']))
else:
    print(total_stars)
