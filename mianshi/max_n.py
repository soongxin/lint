def max_n_num(alist, n):
    # 取出数组中的前n个数
    max_n_list = [alist[i] for i in range(n)]
    # 将取出的长度为n的数组排序,倒序排列
    max_n_list.sort(reverse=True)
    # 剩余的数从左向右依次比较
    for i in range(n, len(alist)):
        # 排序要的数依次与当前的值比较
        for j in range(n-1, -1, -1):
            if alist[i] <= max_n_list[j]:
                # 当前数小于
                if j != n-1:
                    max_n_list[j+1] = alist[i]
                    break
            else:
                if j == 0:
                    max_n_list[j] = alist[i]
                    continue
    return max_n_list

if __name__ == '__main__':
    test_list = [n for n in range(10)]
    print(test_list)
    max_n = max_n_num(test_list, 3)
    print(max_n)