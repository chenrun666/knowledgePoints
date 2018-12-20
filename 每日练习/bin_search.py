def bin_search(n, li):
    low = 0
    height = len(li) - 1
    while low <= height:
        mid = (low + height) // 2
        if li[mid] > n:
            height = mid - 1
        elif li[mid] < n:
            low = mid + 1
        else:
            return None

    return None


def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


def select_sort(li):
    for i in range(len(li) - 1):
        min_pos = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        li[i], li[min_pos] = li[min_pos], li[i]


def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]

    li[left] = tmp
    return left


import random

li1 = list(range(10))
random.shuffle(li1)

# bubble_sort(li1)

# select_sort(li1)

insert_sort(li1)

# quick_sort(li1, 0, len(li1) - 1)

print(li1)
