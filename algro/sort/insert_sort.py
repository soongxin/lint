def insert_sort(alist):
    """
    插入排序算法
    :param alist: 需要排序的数组
    :return: 排序完成的数组
    """
    for i in range(1, len(alist)):
        # 第i次循环时, 列表前i个元素为一个排序好的数组, 将第i+1个数插入到前面合适的位置
        key = i
        for j in range(i-1, -1, -1):
            if alist[key] > alist[j]:
                break
            alist[key], alist[j] = alist[j], alist[key]
            key -= 1

    return alist

if __name__ == '__main__':
    test_list = [i for i in range(20, -1, -1)]
    print(insert_sort(test_list))