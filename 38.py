
from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        def nextTerm(s):
            return "".join(str(len(list(g))) + k for k, g in groupby(s))
        
        result = "1"
        for _ in range(n - 1):
            result = nextTerm(result)
        return result