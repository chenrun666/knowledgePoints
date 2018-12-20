list1 = [1,2,3,4,5,6,7]
list2 = list1[2:5]
print(id(list2), id(list1))
list2[0] = 9999
print(list1)
print(list2)