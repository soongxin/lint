from utlis.timecounter import timecounter


@timecounter
def insert_sort(arr):
    """
    insert sort
    :param arr: array to sort
    :return: sorted array
    """
    # outer loop: i from second element to the end
    for i in range(1, len(arr)):
        key = arr[i]
        # inner loop: j from the last element in sorted sub array to the begin
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr


if __name__ == '__main__':
    result = insert_sort([6, 5, 4, 3, 2, 1])
    print(result)