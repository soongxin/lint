def index_of_min(arr):
    index = 0
    min_num = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_num:
            index = i
            min_num = arr[i]

    return index


if __name__ == '__main__':
    res = index_of_min([9, 8, 7, 6, -1, 5, 4, -5, 2, 1])
    print(res)