from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:(m+n)] = nums2[:n]
        nums1.sort()


# 測試
sol = Solution()

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m, n = 3, 3

sol.merge(nums1, m, nums2, n)
print(nums1)   # 預期輸出 [1,2,2,3,5,6]
        


        
        
    


        
        