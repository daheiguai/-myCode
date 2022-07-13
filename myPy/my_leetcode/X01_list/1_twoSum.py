from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_list = []
        temp = 0
        for i in range(len(nums)):
            if nums[i] > target:
                continue
            if temp+nums[i] == target:
                return [temp_list[-1][0],i]
            temp = nums[i]
            temp_list.append([i,nums[i]])

        for i in range(len(temp_list)-1):
            for j in range():
                pass