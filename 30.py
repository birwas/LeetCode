from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLength = len(words[0])
        numWords = len(words)
        wordFreq = {}
        for word in words:
            wordFreq[word] = wordFreq.get(word, 0) + 1
        
        result = []
        
        for offset in range(wordLength):
            left = offset
            count = 0
            seen = {}
            for right in range(offset, len(s) - wordLength + 1, wordLength):
                word = s[right:right + wordLength]
                if word in wordFreq:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    
                    while seen[word] > wordFreq[word]:
                        leftWord = s[left:left + wordLength]
                        seen[leftWord] -= 1
                        count -= 1
                        left += wordLength
                    
                    if count == numWords:
                        result.append(left)
                        leftWord = s[left:left + wordLength]
                        seen[leftWord] -= 1
                        count -= 1
                        left += wordLength
                else:
                    seen.clear()
                    count = 0
                    left = right + wordLength
        
        return result