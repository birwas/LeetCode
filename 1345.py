from collections import defaultdict, deque
from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        graph = defaultdict(list)        
        for i, val in enumerate(arr):
            graph[val].append(i)

        visited = {0}
        queue = deque([0])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
            
                if i == n - 1:
                    return steps
                
                neighbours = [i - 1, i + 1] + graph[arr[i]]
                graph[arr[i]] = []
                
                for j in neighbours:
                    if 0 <= j < n and j not in visited:
                        visited.add(j)
                        queue.append(j)
            
            steps += 1
        return steps