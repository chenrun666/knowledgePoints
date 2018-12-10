"""
列表被分为有序区和无序区两个部分，最初有序区只有一个元素
每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空
5   7   6   3
j   i
    tmp
"""
import random


def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


li = list(range(10))
random.shuffle(li)
insert_sort(li)
print(li)
