def bubble_sort(alist):
    """
    冒泡排序算法, 在列表原处排序
    :param alist: 需要排序的列表
    :return: 排序完成的列表
    """
    # 外层循环, 从列表的最后一个数循开始,每次循环减一
    for i in range(len(alist)-1, -1, -1):
        # 内层循环, 从列表的第一个数开始, 到外层循环的倒数第二个数结束
        for j in range(i):
            # 比较相邻的两个数, 如果符合条件, 交换两个数的位置
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

    return alist

if __name__ == '__main__':
    test_list = [i for i in range(20, -1, -1)]
    print(bubble_sort(test_list))