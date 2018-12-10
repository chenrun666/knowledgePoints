# 二分查找,时间复杂度为O(logn)
def bin_search(n, li):
    """
    二分查找
    :param n: 查找的内容
    :param li: 有序列表
    :return:
    """
    low = 0
    height = len(li) - 1
    while low <= height:
        mid = (low + height) // 2
        if li[mid] > n:
            height = mid - 1
        elif li[mid] < n:
            low = mid + 1
        else:
            return mid
    return None


def bin_search_rec(data_set, value, low, height):
    if low <= height:
        mid = (low + height) // 2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] > value:
            return bin_search_rec(data_set, value, low, mid - 1)
        else:
            return bin_search_rec(data_set, value, mid + 1, height)

    else:
        return


# python内置查找
li = [
    {"id": 1001, "name": "1"},
    {"id": 1002, "name": "1"},
    {"id": 1004, "name": "1"},
    {"id": 1003, "name": "1"},
]

li.sort(key=lambda x: x["id"], reverse=True)
print(li)
