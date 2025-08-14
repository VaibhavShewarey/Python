a = [{'name': 'kate', 'age': 25}]
b = {'name': 'Nikki', 'age': 30}
a.append(b)
print(a)


c = [{'name': 'kate', 'age': 25}]
d = {'name': 'Nikki', 'age': 30}
c+=[d]
print(c)

e = [{'name': 'kate', 'age': 25}]
f = {'name': 'Nikki', 'age': 30}
e.extend([f])
print(e)

a1 = [{'name': 'kate', 'age': 25}]
b1 = {'name': 'Nikki', 'age': 30}
c1=a1+[b1]
print(c1)


