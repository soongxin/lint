def trailingZeros(num):
    """
    :param num: int
    :return: num的阶乘最后0的个数
    """
    count = 0
    while num != 0:
        num //= 5
        count += num
    return count

if __name__ == '__main__':
    print(trailingZeros(23456787654345678765))