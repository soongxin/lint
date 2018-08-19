from random import randint
from copy import deepcopy

TEST_ARR_LENGTH = 200


class Sort(object):
    """Sort class contains some sort methods"""
    def __init__(self, arr):
        self.arr = deepcopy(arr)

    def fast_sort(self, arr):
        # 在类表中找一个基点
        mid_index = len(arr) // 2
        # 将列表中小于基准点的项放到基准左侧,大于基准的放在右侧,基准点位置确定
        for i in range(0, len(arr)):
            if arr[i] < arr[mid_index]:
                arr.insert(0, )
        # 对两端的列表分别递归调用fast_sort
        # 列表排序好的话,结束递归调用
        pass

    def insert_sort(self):
        """
            insert sort
            :param arr: array to sort
            :return: sorted array
            """
        # outer loop: i from second element to the end
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            # inner loop: j from the last element in sorted sub array to the begin
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1

            self.arr[j + 1] = key

        return self.arr

    def select_sort(self):
        """
        :param arr: array to sort
        :return: sorted array
        """
        for i in range(0, len(self.arr) - 1):
            min_index = i + 1

            for j in range(i + 1, len(self.arr)):
                if self.arr[min_index] > self.arr[j]:
                    min_index = j
            if self.arr[i] > self.arr[min_index]:
                temp = self.arr[i]
                self.arr[i] = self.arr[min_index]
                self.arr[min_index] = temp
        return self.arr

    def bubble_sort(self):
        """
        :param arr: array to sort
        :return: sorted array
        """
        for i in range(0, len(self.arr) - 1):
            for j in range(0, len(self.arr) - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j + 1]
                    self.arr[j + 1] = temp
        return self.arr

    def merge_sort(self):
        return self.merge_sort_static(self.arr)

    @staticmethod
    def merge_sort_static(arr):
        """
            sort an array by merge sort function
            :param arr: the array need to sort
            :return: result: sorted array
            """
        # if array length big than 1, sepreate the array to two sub arrays
        if len(arr) > 1:
            half_index = int(len(arr) / 2)
            arr_1 = arr[:half_index]
            arr_2 = arr[half_index:]

            # sub array call merge_sort function to sort itself
            arr_1 = Sort.merge_sort_static(arr_1)
            arr_2 = Sort.merge_sort_static(arr_2)

            # merge sorted two sub array, return result
            result = Sort.merge(arr_1, arr_2)

            return result

        # if array length is 1, array is sorted, then return itself
        else:
            return arr

    @staticmethod
    def merge(arr_1, arr_2):
        """
            subprogram used in merge sort function
            :param arr_1: first array to merge
            :param arr_2: second array to merge
            :return: merged and sorted array
            """
        # insert a end flag in two arrays
        arr_1.append('inf')
        arr_2.append('inf')

        # define index flag for tow arrays
        index_1 = 0
        index_2 = 0

        # define a contianer to storge result
        result = []

        # try to merge two arrays
        for i in range(0, len(arr_1) + len(arr_2) - 2):
            if arr_1[index_1] != 'inf' and arr_2[index_2] != 'inf':
                if arr_1[index_1] < arr_2[index_2]:
                    result.append(arr_1[index_1])
                    index_1 += 1
                else:
                    result.append(arr_2[index_2])
                    index_2 += 1

            elif arr_1[index_1] == 'inf':
                result.append(arr_2[index_2])
                index_2 += 1
            elif arr_2[index_2] == 'inf':
                result.append(arr_1[index_1])
                index_1 += 1

        return result

    def quick_sort(self):
        pass


if __name__ == '__main__':
    # 定义一个逆序数组
    test_arr = [n for n in range(TEST_ARR_LENGTH, -1, -1)]
    print(test_arr)
    sort = Sort(test_arr)
    result = sort.merge_sort()
    print(result)
