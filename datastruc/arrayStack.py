class Stack(object):
    """使用数组实现一个栈"""
    def __init__(self):
        self.data = []

    def push(self, num):
        """压栈操作"""
        self.data.append(num)

    def pop(self):
        """返回从栈中弹出的元素, 当栈为空的时候, 抛出IndexError"""
        return self.data.pop()

    def peek(self):
        """查看当前栈顶的元素, 当栈为空的时候, 抛出IndexError"""
        return self.data[-1]

    def __len__(self):
        """返回栈的长度, 调用len(obj)时会自动调用obj对象的__len__方法"""
        return len(self.data)

    def isEmpty(self):
        """判断栈是否为空"""
        return True if len(self.data)==0 else False

    def clear(self):
        """清空栈"""
        self.data = []

    def __repr__(self):
        """当前对象的表现形式, 在终点直接键入对象时会调用"""
        return 'Stack_' + str(self.data)

    def __str__(self):
        """当前对象的字符串表示, 使用print(obj)时会调用"""
        return 'Stack_' + str(self.data)


def isBalance(text):
    """栈的应用,检查括号是否平衡"""
    result_stack = Stack()
    for i in text:
        if i in ['{', '[', '(']:
            result_stack.push(i)
        elif i in ['}', ']', ')']:
            # 遇到结束括号的情况
            if result_stack.isEmpty():
                # 如果当前栈为空, 不匹配,返回False
                return False
            chFromStack = result_stack.pop()

            if not ((chFromStack == '{' and i == '}' )
                    or (chFromStack == '[' and i == ']')
                    or (chFromStack == '(' and i == ')')):
                # 如果不满足匹配条件, 则返回False
                return False

    # 遍历结束后, 如果结果栈为空, 则代表括号匹配, 栈不为空, 括号不匹配
    return result_stack.isEmpty()


if __name__ == '__main__':
    print(isBalance('(())'))