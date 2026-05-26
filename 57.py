class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][1]:         
                res[-1][1] = max(res[-1][1], end)
            else:                            
                res.append([start, end])
        
        return res