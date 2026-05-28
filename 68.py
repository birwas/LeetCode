class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        output = []
        i = 0
        while i < len(words):
            length = len(words[i])
            j = i + 1
            while j < len(words) and length + 1 + len(words[j]) <= maxWidth:
                length += 1 + len(words[j])
                j += 1

            wordCount = j - i
            spaces = maxWidth - sum(len(word) for word in words[i:j])

            if j == len(words) or wordCount == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                slots = wordCount - 1
                base, extra = divmod(spaces, slots)
                line = ""
                for k in range(wordCount - 1):
                    line += words[i+k]
                    line += " " * (base + (1 if k < extra else 0))
                line += words[j-1]

            output.append(line)
            i = j

        return output