# 1， python中实现二进制，八进制，十进制，十六进制转换
a1 = "010101010"
print(int(a1, base=2))

# int -> bin
bin(234)

# int -> oct
oct(3445)

# int -> hex
hex(21345)

# 编写一个函数实现将IP地址转换成一个整数
a = int("".join([bin(int(i)).lstrip("0b").zfill(8) for i in "10.0.0.1".split(".")]), 2)
# print(a)
#
# # 2， 逻辑运算
# print(1 or 3)
# print(1 and 3)
# print(0 and 2 and 1)
# print(0 and 2 or 1)
#
# print(2 and 1)
# print(2 or False and 1)

# 3, 三元表达式
"""
v1 = 'x1' if x == 1 else 'x2'
"""

# 4, 常见的数据类型
"""
int
float
str : split, join, strip, upper
list : index, append, pop, insert, extend, reverse
tuple :
set :
dict : get, remove, keys, values, items,clear, del
"""
data_list = [
    {"id": 1, "name": "陈润", "pid": None},
    {"id": 2, "name": "彭慧娴", "pid": None},
    {"id": 3, "name": "傻子", "pid": 1},
    {"id": 4, "name": "王力宏", "pid": 2},
    {"id": 5, "name": "王力宏3", "pid": 2},
    {"id": 6, "name": "王力宏4", "pid": 1},
]
result = []

data_dict = {item["id"]: item for item in data_list}


for index, dic in data_dict.items():
    pid = dic["pid"]
    if not pid:
        dic["children"] = []
        result.append(dic)

    elif pid in data_dict:
        data_dict[pid]["children"].append(dic)
        result.append(data_dict[pid])

# 乘法表
print("\n".join("\t".join([f"{x}*{y}={x*y}" for y in range(1, x+1)]) for x in range(1, 10)))







