class Stack(object):
    def __init__(self, data):
        # data格式为列表, 使用列表实现栈
        self.data = data
        self.min_index = data.index(min(data))
        self.second_min_index = None
        self.length = len(self.data)

    def push(self, n):
        self.data.append(n)
        self.length += 1
        if n < self.data[self.min_index]:
            self.second_min_index = self.min_index
            self.min_index = self.length - 1

    def pop(self):
        if self.second_min_index:
            self.min_index = self.second_min_index

        del self.data[-1]
        self.length -= 1

    def min(self):
        return self.data[self.min_index]

    def __repr__(self):
        return str(self.data)