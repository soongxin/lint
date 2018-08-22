def aplusb(a, b):
    """
    @param a: int
    @param b: int
    @return: The sum of a and b
    """
    while(b!=0):
        _a = a ^ b
        _b = (a & b) << 1
        a = _a
        b = _b

    return a


if __name__ == '__main__':
    print(aplusb(10, -10))