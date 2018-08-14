from datastruc.node import Node


# 构造一个单链表
head = None
for i in range(1, 11):
    head = Node(i, head)


if __name__ == '__main__':
    """
        while head != None:
        print(head)
        head = head.next

    # 遍历一次后, head为None, 该语句不会被执行
    while head != None:
        print(head)
        head = head.next
    """
    # 使用临时变量指向链表的开始处, 称为哨兵
    probe = head
    while probe !=None:
        print(probe.data)
        probe = probe.next

    # 使用临时变量指向链表的开始处, 称为哨兵
    probe = head
    while probe !=None:
        print(probe.data)
        probe = probe.next


