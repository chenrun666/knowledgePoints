import random


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


li = list(range(10))

random.shuffle(li)

# bubble_sort(li)
select_sort(li)


# print(li)


def pi():
    count = 0
    n = 10000000

    for i in range(n):
        x = (random.random() - 0.5) * 2
        y = (random.random() - 0.5) * 2

        if (x ** 2 + y ** 2) < 1:
            count += 1

    pi = 4 * count / n
    print(pi)


pi()
