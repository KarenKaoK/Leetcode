class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_json = {}

        for num in nums:
            if num not in nums_json.keys():
                nums_json[num] = 1
            else:
                nums_json[num] +=1

        for k in nums_json.keys():
            if nums_json[k] == max(list(nums_json.values())):
                return k


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        count = 0
        for x in nums:
            if count == 0:
                cand = x
            count += 1 if x == cand else -1
        return cand