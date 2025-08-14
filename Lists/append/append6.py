a=[1,2,3]
a.extend([4,5,6])
print(a)
b=[1,2,3]
b+=[4,5,6]
print(b)


a = [1, 2, 3]
b = [4, 5, 6]

for i in b:
    a.append(i)
print(a)


c=[1,2,3]
c=[*c,4,5]
print(c)