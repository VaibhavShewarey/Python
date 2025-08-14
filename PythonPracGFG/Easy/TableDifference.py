#User function Template for python3
n1 = int(input())
n2 = int(input())

# Your code here

li3=[]
for i in range(1,11):
    diff=n1*i-n2*i
    li3.append(diff)
    

print(*li3)
