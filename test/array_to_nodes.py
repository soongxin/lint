# 将一个填满的数组中的项, 转移到一个单链表结构中,这个操作应该保留
# 这些想的书序不变
from datastruc.arrays import Array
from datastruc.node import Node


# 构造一个数组
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = Array(10)
for i in range(0, 10):
    arr[i] = i + 1


if __name__ == '__main__':
    # 构造链表, 并倒序将数组中的值插入链表中
    head = None
    for i in range(len(arr)-1, -1, -1):
        head = Node(arr[i], head)

    # 输出链表
    while head != None:
        print(head.data)
        head = head.next