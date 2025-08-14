x=int(input())
y=int(input())
#code here
x=int(x)
y=int(y)
x=max(-100,min(x,100))
y=max(-100,min(y,100))

p=int(x)+int(y)
q=int(x)-int(y)
r=int(x)*int(y)
s=int(x)//int(y)
t=int(x)%int(y)

print(p,q,r,s,t)