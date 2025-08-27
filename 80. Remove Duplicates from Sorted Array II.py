class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        else:
            point = 0
            fill = 0

            while point <=len(nums)-1:
                if point <= 1:
                    nums[fill] = nums[point]
                    fill +=1 
                    point += 1    
                else:
                    if nums[point] != nums[fill-2]:
                        nums[fill] = nums[point]
                        point+=1
                        fill+=1
                    else:
                        point+=1
            return fill