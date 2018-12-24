class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def bin_search(n, li):
    low = 0
    height = len(li) - 1
    while low <= height:
        mid = (low + height) // 2
        if li[mid] > n:
            height = mid
        elif li[mid] < n:
            low = mid
        else:
            return mid

    return None
