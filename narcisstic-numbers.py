def narcissistic(value):
    x = str(value)
    n = len(x)
    f = 0
    for v in map(int,x):
        f = f + v**n
    if f == value:
        return True
    else:
        return False
