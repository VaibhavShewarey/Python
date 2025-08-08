import copy
original={'name':'Alice','marks':{'math':90,'science':95}}

shallow=copy.copy(original)

shallow['marks']['math']=100

print("Original:",original)
print("Shallow copy: ",shallow)