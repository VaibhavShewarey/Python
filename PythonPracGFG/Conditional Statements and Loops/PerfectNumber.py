class Solution:
    def isPerfect(self, n):
        a=1
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                a+=i
                if i!=n//i:
                    a+=n//i
        return n==a