# copy, deepcopy, [:]
a = [1,2,3]
b = a[:]
print(a, b)
a[0] = 4
print(a, b)

a = [1,2,3]
b = a
print(a, b)
a[0] = 4
print(a, b)