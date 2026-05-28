class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lastLowerCase = {}
        firstUpperCase = {}

        for i, c in enumerate(word):
            if c.islower():
                lastLowerCase[c] = i
            elif c.lower() not in firstUpperCase:
                firstUpperCase[c.lower()] = i
        
        count = 0
        for c in lastLowerCase:
            if c in firstUpperCase and lastLowerCase[c] < firstUpperCase[c]:
                count += 1
        return count