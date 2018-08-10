class Counter(object):

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def __str__(self):
        return str(self.count)