set1={1,2,3,4,5}
set1.remove(3)
print(set1)

try:
    set1.remove(10)
except KeyError as e:
    print("Error: ",e)

set1.discard(4)
print(set1)

set1.discard(10)
print(set1)

