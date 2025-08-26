
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        point = 0
        fill = 0 
        while point <len(nums):

            if nums[point] != val:
                nums[fill] = nums[point]
                fill += 1
                point += 1
            
            else:
                point+=1

        return fill
 
 # 測試1
sol = Solution()

nums = [2,3,3,2]
val = 2


k = sol.removeElement(nums, val)
print(nums[:k])   # 預期輸出 [3,3]