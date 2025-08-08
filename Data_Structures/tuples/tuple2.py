tup=(5,'Welcome',7,'Geeks')
print(tup)

tup1=(0,1,2,3)
tup2=('python','geek')
tup3=(tup1,tup2)
print(tup3)

tup1=('Geeks',)*3
print(tup1)

tup=('Geeks')
n=5
for i in range(int(n)):
    tup=(tup,)
    print(tup)