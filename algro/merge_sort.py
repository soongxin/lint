from random import randint
from utlis.timecounter import timecounter


def merge(arr_1, arr_2):
    """
    subprogram used in merge sort function
    :param arr_1: first array to merge
    :param arr_2: second array to merge
    :return: merged and sorted array
    """
    # insert a end flag in two arrays
    arr_1.append('inf')
    arr_2.append('inf')

    # define index flag for tow arrays
    index_1 = 0
    index_2 = 0

    # define a contianer to storge result
    result = []

    # try to merge two arrays
    for i in range(0, len(arr_1)+len(arr_2)-2):
        if arr_1[index_1] != 'inf' and arr_2[index_2] != 'inf':
            if arr_1[index_1] < arr_2[index_2]:
                result.append(arr_1[index_1])
                index_1 += 1
            else:
                result.append(arr_2[index_2])
                index_2 += 1

        elif arr_1[index_1] == 'inf':
            result.append(arr_2[index_2])
            index_2 += 1
        elif arr_2[index_2] == 'inf':
            result.append(arr_1[index_1])
            index_1 += 1

    return result


def merge_sort(arr):
    """
    sort an array by merge sort function
    :param arr: the array need to sort
    :return: result: sorted array
    """
    # if array length big than 1, sepreate the array to two sub arrays
    if len(arr) > 1:
        half_index = int(len(arr)/2)
        arr_1 = arr[:half_index]
        arr_2 = arr[half_index:]

        # sub array call merge_sort function to sort itself
        arr_1 = merge_sort(arr_1)
        arr_2 = merge_sort(arr_2)

        # merge sorted two sub array, return result
        result = merge(arr_1, arr_2)

        return result

    # if array length is 1, array is sorted, then return itself
    else:
        return arr


if __name__ == '__main__':
    # test merge function
    # result = merge([9, 10, 13], [2, 4, 5, 6, 7])

    # test merge_sort function, generate a random list for test
    arr = [randint(0, 10) for i in range(0, 10)]
    result = merge_sort(arr)
    print(result)

