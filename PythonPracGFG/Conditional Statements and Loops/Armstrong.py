class Solution:
    def armstrongNumber (self, n):
        # code here 
        s=0
        t=n
        while n:
            m=n%10
            s=s+m**3
            n=int(n/10)
        
        if s==t:
            return True
        else:
            return False