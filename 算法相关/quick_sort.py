"""
去一个元素p（第一个元素），使元素p归位
"""
import random


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


def quick_sort_reverse(li, left, right):
    if left < right:
        mid = reverse(li, left, right)
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


def reverse(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] <= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] >= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


li = list(range(100))
random.shuffle(li)
# print(li)
quick_sort(li, 0, len(li) - 1)

print(li)
