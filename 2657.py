def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
    count = {}
    common = 0
    result = []

    for a, b in zip(A, B):
        count[a] = count.get(a, 0) + 1
        if count[a] == 2:   
            common += 1

        count[b] = count.get(b, 0) + 1
        if count[b] == 2:   
            common += 1

        result.append(common)

    return result