def merge(alist, blist):
    # 合并两个数组
    alist.append('infi')
    blist.append('infi')
    # 存储结果的列表
    result = []
    # 当前索引
    index_a = 0
    index_b = 0
    for i in range(len(alist) + len(blist) - 2):
        if alist[index_a] != 'infi' and blist[index_b] != 'infi':
            if alist[index_a] < blist[index_b]:
                result.append(alist[index_a])
                index_a += 1
            else:
                result.append(blist[index_b])
                index_b += 1
        else:
            if alist[index_a] == 'infi':
                result.append(blist[index_b])
                index_b += 1
            else:
                result.append(alist[index_a])
                index_a += 1

    return result



if __name__ == '__main__':
    a = [2, 4, 6, 8, 10, 11, 23 ,23 ,45,55]
    b = [1, 3, 5, 7, 9, 10000]
    result = merge(a, b)
    print(result)