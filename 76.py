class Solution:
    def minWindow(self, s: str, t: str) -> str:
        characters = {}
        for c in t:
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1
        left,right = 0,0
        window = {}
        have = 0
        result = [-1, -1]
        
        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in characters and window[s[right]] == characters[s[right]]:
                have += 1
            while have == len(characters):
                result = [left,right] if result[0] == -1 or right -left < result[1] - result[0] else result
                window[s[left]] -= 1
                if s[left] in characters and window[s[left]] < characters[s[left]]:
                    have -= 1
                left += 1
            right += 1
        return "" if result[0] == -1 else s[result[0]:result[1]+1]