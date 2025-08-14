a=[2,5,6,7]
a.append(8)
print(a)

b=[2,5,6,7]
b.append(True)
print(b)

c=[2,5,6,7]
c.append([1,3,4])
print(c)

d=[]
for i in range(5):
    d.append(i)
print(d)

e=[2,5,6,7]
e.append([1,3,4])
print(e)

f=[2,5,6,7]
f.extend([1,3,4])
print(f)