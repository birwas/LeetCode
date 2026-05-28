class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
     
        def binarySearch(arr, target):
            left, right = 0, len(arr) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return False
        
        left, right = 0, len(matrix) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return binarySearch(matrix[mid], target)
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False