def aplusb(a, b):
    """
    @param a: int
    @param b: int
    @return: The sum of a and b
    """
    # 将数字转换成二进制字符串
    str_a = bin(a)
    str_b = bin(b)
    # 结果最大长度为加数最长的加一
    res_len = max(len(str_a), len(str_b)) - 1
    print(res_len)

    for i in range(-1, -res_len - 1, -1):
        print(str_b[i])
        print(str_b[i])

    return None


if __name__ == '__main__':
    aplusb(100, 9)

# hello world