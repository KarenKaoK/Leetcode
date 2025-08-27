from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1 

        else:
            point = 0
            fill = 0

            while point <=len(nums)-1:
                if point == 0:
                    nums[fill] = nums[point]
                    fill +=1 
                    point += 1    
                else:
                    if nums[point] != nums[fill-1]:
                        nums[fill] = nums[point]
                        point+=1
                        fill+=1
                    else:
                        point+=1

            return fill