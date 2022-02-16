import re

input = input()
ops = re.findall(r'\W+\d*', input)
strings = re.split(r'\W+\d*', input)
strings.pop()

for idx in range(len(strings)):
    st = strings[idx]
    opr = ops[idx][0]
    cases = {
        '+': 'tighten',
        '-': 'loosen'
    }
    opr_word = cases[opr]

    print(" ".join([st, opr_word, ops[idx][1:]]))

