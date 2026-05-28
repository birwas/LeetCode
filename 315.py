class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n=len(nums)
        counts=[0]*n
        indexes=list(range(n))
        
        def mergeSort(indexList):
            if len(indexList)<=1:
                return indexList
            mid=len(indexList)//2
            left=mergeSort(indexList[:mid])
            right=mergeSort(indexList[mid:])
            return merge(left,right)

        def merge(left,right):
            result=[]
            l,r=0,0
            
            while l<len(left) and r<len(right):
                if nums[right[r]]<nums[left[l]]:
                    result.append(right[r])
                    r+=1
                else:
                    counts[left[l]]+=r
                    result.append(left[l])
                    l+=1
            while l<len(left):
                counts[left[l]]+=r
                result.append(left[l])
                l+=1
            result.extend(right[r:])
            return result
        
        mergeSort(indexes)
        return counts