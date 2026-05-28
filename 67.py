class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            val = carry
            if i >= 0:
                val += int(a[i])
                i -= 1
            if j >= 0:
                val += int(b[j])
                j -= 1
            carry = val // 2
            result.append(str(val % 2))

        return "".join(reversed(result))