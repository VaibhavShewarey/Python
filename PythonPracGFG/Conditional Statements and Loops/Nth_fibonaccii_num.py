class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        a=0
        b=1
        while n:
            fib=a+b
            a,b=b,a+b
            n=n-1
        return a