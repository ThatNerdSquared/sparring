def move_zeros(array):
    b = list(filter(lambda x: x != 0, array))
    a = list(array.count(0) * [0])
    return b + a
