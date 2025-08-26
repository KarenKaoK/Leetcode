from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:(m+n)] = nums2[:n]
        nums1.sort()

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m+n -1 
        while m > 0 and n > 0:
   
            if nums1[m-1] > nums2[n-1]:
                nums1[k] = nums1[m-1]
                m -=1 
                k -=1 
            else:
                nums1[k] = nums2[n-1]
                n -= 1
                k -=1 
        if n >0 :
            nums1[:n] = nums2[:n]

# 測試1
sol = Solution()

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m, n = 3, 3

sol.merge(nums1, m, nums2, n)
print(nums1)   # 預期輸出 [1,2,2,3,5,6]

# 測試2
sol = Solution()

nums1 = [1,4,5,0,0,0]
nums2 = [1,2,6]
m, n = 3, 3

sol.merge(nums1, m, nums2, n)
print(nums1)   # 預期輸出 [1,1,2,4,5,6]

# 測試2
sol = Solution()

nums1 = [0]
nums2 = [1]
m, n = 0, 1

sol.merge(nums1, m, nums2, n)
print(nums1)   # 預期輸出 [1]
        


        
        
    


        
        