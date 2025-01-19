a = [1, 2, 4, 5, 6]
b = a
print(a)
print(b)
del a[0]
print(id(a))
print(id(b))
c=a[:]
print(id(a))
print(id(b))
print(id(c))
a.append(7)
print((a))
print((b))
print((c))


