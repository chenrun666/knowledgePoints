"""
一趟遍历记录最小的数字，放到第一个位置
再一趟遍历记录剩余列表中最小的数字，继续放置
交换次数少，比冒泡相对快一点
"""
import random


def find_min(li):
    min_val = li[0]
    for i in range(1, len(li)):
        if li[i] < min_val:
            min_val = li[i]
    return min_val


def find_min_pos(li):
    min_val_pos = 0
    for i in range(1, len(li)):
        if li[i] < li[min_val_pos]:
            min_val_pos = i
    return min_val_pos


def select_sort(li):
    for i in range(len(li) - 1):
        # 无序区的范围
        min_pos = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        li[i], li[min_pos] = li[min_pos], li[i]


li = list(range(10))
random.shuffle(li)
select_sort(li)
print(li)
