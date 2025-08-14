import itertools

a = [1, 2]
b = [3, 4]
c = [5, 6]

e=list(itertools.chain(a,b,c))
print(e)


a1 = [1, 2]
b1 = [3, 4]
c1 = [5, 6]
a1.extend(b)
a1.extend(c)
print(a1)

a2 = [1, 2]
b2 = [3, 4]
c2 = [5, 6]
a2=a2+b2+c2
print(a2)

a3 = [1, 2]
b3 = [3, 4]
c3 = [5, 6]
p=[x for lst in [a3,b3,c3] for x in lst]
print(p)

a4 = [1, 2]
b4 = [3, 4]
c4 = [5, 6]
f=[item for sublist in zip(a4,b4,c4) for item in sublist]
print(f)

a = [1, 2]
b = [3, 4]
c = [5, 6]
s=[]
for gst in [a,b,c]:
    for item in gst:
        s.append(item)
print(s)



        