li=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sli=li[1]
sli.append(10)
print(li)

i=1
li[i]=[item for item in li[i]]+[11]
print(li)


li[i].extend([12])
print(li)

li[i].insert(len(li[i]),13)
print(li)