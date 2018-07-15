from algro.merge_sort import merge_sort
from algro.insert_sort import insert_sort
from utlis.timecounter import timecounter


LENGTH = 10000


@timecounter
def sort(arr):
    result = merge_sort(arr)
    return result


if __name__ == '__main__':
    arr = [i for i in range(LENGTH, 0, -1)]
    result = sort(arr)
    # result2 = insert_sort(arr)
    # print(arr)
    print(result)
