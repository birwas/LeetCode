class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sPosition= 0
        pPosition= 0
        starPosition= -1
        starMatchPosition= -1
        while sPosition < len(s):
            if pPosition < len(p) and (p[pPosition] == s[sPosition] or p[pPosition] == '?'):
                sPosition += 1
                pPosition += 1
            elif pPosition < len(p) and p[pPosition] == '*':
                starPosition= pPosition
                starMatchPosition= sPosition
                pPosition += 1
            elif starPosition != -1:
                starMatchPosition += 1
                sPosition= starMatchPosition
                pPosition= starPosition + 1
            else:
                return False
        
        while pPosition < len(p) and p[pPosition] == '*':
            pPosition += 1
        return pPosition == len(p)