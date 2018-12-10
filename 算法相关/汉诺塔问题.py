"""
汉诺塔移动次数的递推式：h(x)=2h(x-1)+1
h(64)=18446744073709551615

n 个盘子时：
1， 把n-1个圆盘从A经过C移动到B
2， 把第n个盘子从A移动到C
3， 把n-1个圆盘从B经过A移动到C
"""


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print(f"{a} -> {c}")
        hanoi(n - 1, b, a, c)


hanoi(3, "A", "B", "C")


# 斐波那契数列
# 1，1，2，3，5，8，13
def fib_re(n):
    if n == 0 or n == 1:
        return 1

    return fib_re(n - 1) + fib_re(n - 2)


def fib_list(n):
    li = [1, 1]

    for i in range(2, n + 1):
        li.append(li[-1] + li[-2])

    return li[-1]


def fib(n):
    if n == 0 or n == 1:
        return n

    a, b, c = 1, 1, 1

    for num in range(2, n + 1):
        a = b
        b = c
        c = a + b
    return c


print(fib(100))

# 面试题：走楼梯问题
# f(n) = f(n-1) + f(n-2)
