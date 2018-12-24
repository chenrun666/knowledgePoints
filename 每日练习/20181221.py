def bin_search(n, li):
    low = 0
    height = len(li) - 1
    while low <= height:
        mid = (low + height) // 2
        if n < li[mid]:
            height = mid - 1
        elif n > li[mid]:
            low = mid + 1
        else:
            return None

    return None


def bubble_sort(li):
    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


def select_sort(li):
    for i in range(len(li) - 1):
        min_pos = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        li[min_pos], li[i] = li[i], li[min_pos]


def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


import random

li = list(range(10))
random.shuffle(li)
# bubble_sort(li)
select_sort(li)
# insert_sort(li)
print(li)
