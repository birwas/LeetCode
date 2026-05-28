class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def combinations(start, current):
            if len(current) == k:
                result.append(current[:])
                return
            for num in range(start, n+1):
                current.append(num)
                combinations(num+1, current)
                current.pop()
        
        combinations(1, [])
        return result