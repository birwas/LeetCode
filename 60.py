class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        numbers = list(range(1, n + 1))
        k -= 1  
        permutation = []
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            index = k // f
            permutation.append(str(numbers[index]))
            numbers.pop(index)
            k %= f
        return ''.join(permutation)