set1={3,1,4,1,5,9,2}
print(set1)

try:
    print(set1[0])
except TypeError as e:
    print(e)