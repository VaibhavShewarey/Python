from collections import deque
from functools import reduce

li=deque([1,3,4,5,7])
li.appendleft(6)
print(list(li))

vi=[1,3,4,5,7]
vi.insert(0,6)
print(vi)

ti=[1,3,4,5,7]
ti=[6]+ti
print(ti)

gi=[1,3,4,5,7]
gi=[6]+gi[:]
print(gi)



ci=[1,3,4,5,7]
ci=reduce(lambda x,y:[6]+x+y,[[],ci])
print(ci)