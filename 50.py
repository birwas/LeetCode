class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        def recur(x,n):
            if n==0:
                return 1
            if n%2==0:
                half = recur(x,n//2)
                return half*half
            else:
                return x*recur(x,n-1)
        return recur(x,n)