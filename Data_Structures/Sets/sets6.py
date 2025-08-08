set1={1,2,3,4,5}
val=set1.pop()
print(val)
print(set1)

set1.clear()
try:
    set1.pop()
except KeyError as e:
    print("Error: ",e)