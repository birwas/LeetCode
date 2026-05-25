def longestCommonPrefix(arr1, arr2):
    seen = set()
    for x in arr1:
        while x > 0:
            seen.add(x)
            x //= 10
            
    longest=0
    for x in arr2:
        while x > 0:
            if x in seen:
                longest = max(longest, len(str(x)))
                break
            x //= 10
    return longest