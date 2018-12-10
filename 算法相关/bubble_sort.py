"""
冒泡排序
列表两个相邻的数，如果前面的比后面的数字大，那么交换两个数。
这样一趟走完之后，最大的数字就出来了。

时间复杂度为：O(n^2)
"""
import random


def bubble_sort(li):
    len_num = len(li)
    for i in range(len_num - 1):
        for j in range(len_num - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


li = list(range(10))
random.shuffle(li)
after_li = bubble_sort(li)
print(after_li)


# 改进之后的冒泡：最好情况的时间复杂度为O(n)
def bubble_sort2_(li):
    len_num = len(li)
    for i in range(len_num - 1):
        exchange = False
        for j in range(len_num - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            break
    return li
