# 自定义数组结构


class Array(object):
    """自定义数组类"""

    def __init__(self, len, default=None):
        """
        数组初始化
        :param len: 数组的长度
        :param default: 数组的默认值
        """
        self._item = list()
        for i in range(len):
            self._item.append(default)

    def __str__(self):
        """使用打印输出的时候的返回值"""
        return self._item.__str__()

    def __len__(self):
        """调用len(obj)时的返回值"""
        return len(self._item)

    def __iter__(self):
        """调用迭代环境时返回迭代器"""
        return iter(self._item)

    def __getitem__(self, item):
        """通过索引取值时的返回值"""
        return self._item[item]

    def __setitem__(self, key, value):
        """通过索引设置值"""
        self._item[key] = value


if __name__ == "__main__":
    a = Array(10)
    print(a)