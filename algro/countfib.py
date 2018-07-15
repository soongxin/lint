class Counter(object):

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def __str__(self):
        return str(self.count)


def fib(n ,counter):
    """Count the number of calls of the Fibonacci function"""
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n-1, counter) + fib(n-2, counter)


problemSize = 2
print("%12s%15s" % ("Problem Size", "Calls"))

for count in range(5):
    counter = Counter()

    # the start of the algorithm
    fib(problemSize, counter)
    # the end of the algorithm

    print("%12s%15s" % (problemSize, counter))
    problemSize *= 2


# if __name__ == '__main__':
#