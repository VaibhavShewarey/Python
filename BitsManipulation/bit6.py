n=29
count=0
while n:
    n=n&(n-1)
    count+=1
print("Set bits:",count)