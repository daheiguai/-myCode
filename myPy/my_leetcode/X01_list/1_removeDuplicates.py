from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            i = 0
            l = len(nums)-1
            while i < l:
                if nums[i] == nums[i+1]:
                    nums.pop(i) #问题：删除数组内的东西很耗内存，题目只要求计数
                    l -= 1
                    continue
                i += 1
            return len(nums) #这个len函数可以不使用，用 l 来代替  以后尽量只用一次len
        return 0

#别人的解
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 0
#         for j in range(1, len(nums)):
#             if nums[j] != nums[i]:
#                 i += 1
#                 nums[i] = nums[j]
#         return i + 1



if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))