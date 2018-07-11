def trailingZeros(num):
    """
    :param num: int
    :return: num的阶乘最后0的个数
    """
    result = 1
    for i in range(1, num+1):
        result *= i

    result = str(result)

    count = 0
    for i in range(-1, -len(result), -1):
        if result[i] == '0':
            count += 1
        else:
            break

    return count


print(trailingZeros(10))