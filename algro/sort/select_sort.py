def select_sort(alist):
    """
    选择排序算法实现
    :param alist: 需要排序的列表
    :return: 排序后的列表
    """
    for i in range(1, len(alist)):
        min = i - 1
        for j in range(i, len(alist)):
            if alist[j] < alist[min]:
                min = j
        alist[min], alist[j] = alist[j]