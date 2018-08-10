from utlis.counter import Counter


def floor_two(problemSize, counter):
    while problemSize > 0:
        counter.increment()
        problemSize = problemSize // 2


if __name__ == '__main__':
    problemSize = 1000
    print("%12s%15s" % ('problem size', 'calls'))
    for i in range(9):
        counter = Counter()
        floor_two(problemSize, counter)
        problemSize *= 10

        print("%12s%15s" % (problemSize, counter))
