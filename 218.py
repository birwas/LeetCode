import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height))   
            events.append((right, +height))  

        events.sort()
        
        buildingCount = {}
        heap = []
        result = []
        
        prevMaxHeight = 0
        for x, height in events:
            if height < 0:
                heapq.heappush(heap, height)
                buildingCount[height] = buildingCount.get(height, 0) + 1
            else:
                buildingCount[-height] = buildingCount.get(-height, 0) - 1
            
            while heap and buildingCount[heap[0]] == 0:
                heapq.heappop(heap)
            
            currentMaxHeight = -heap[0] if heap else 0
            if currentMaxHeight != prevMaxHeight:
                prevMaxHeight = currentMaxHeight
                result.append([x, currentMaxHeight])
        
        return result