import copy
original = {'name':'Alice','marks':{'math':90,'science':95}}

deep=copy.deepcopy(original)
deep['marks']['math']=100

print("Original:",original)
print("deep copy:",deep)