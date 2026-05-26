class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        if not s:
            return False
        number=False
        decimalPoint=False
        exponent=False
        for i in range(len(s)):
            if s[i] in ['+','-']:
                if i>0 and s[i-1] not in ['e','E']:
                    return False
                if i==len(s)-1:
                    return False
            elif s[i]=='.':
                if decimalPoint or exponent:
                    return False
                decimalPoint=True
            elif s[i] in ['e','E']:
                if exponent or not number or i==len(s)-1:
                    return False
                exponent=True
            elif s[i].isdigit():
                number=True
            else:
                return False
        return number