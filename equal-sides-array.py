def find_even_index(arr):
    for i in range(len(arr)):
        print(arr[i+1:len(arr)+1])
        if sum(arr[:i]) == sum(arr[i+1:len(arr)]):
            return i
    return -1
