import sys

def generate_data(prevnum, pagenum, current_route):
    if pagenum not in data['checked_pages']:
        data['checked_pages'].append(pagenum)
        if data['pages'][str(pagenum)] == []:
            data['routes'].append(current_route)
        else:
            current_route += 1
            for num in data['pages'][str(pagenum)]:
                if num != prevnum:
                    generate_data(pagenum, num, current_route)

raw_input = sys.stdin
input = []
for line in sys.stdin:
    input.append(line.rstrip())

data = {
    'page_num': int(input[0]),
    'is_circular': True,
    'checked_pages': [],
    'routes': [],
    'pages': {}
}

input.pop(0)

for n in range(data['page_num']):
    pagespec = input[n].split()
    pagespec.pop(0)
    data['pages'][str(n+1)] = list(map(int, pagespec))

generate_data(None, 1, 1)

for item in data['pages'].keys():
    if int(item) not in data['checked_pages']:
        data['is_circular'] = False

print('Y') if data['is_circular'] else print('N')
print(min(data['routes']))
