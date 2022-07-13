from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        a = nums[k-k*2:]+nums[:len(nums)-k]
        for i in range(len(nums)):
            nums[i] = a[i]
        # return nums

if __name__ == "__main__":
    s = Solution()
    print(s.rotate([1,2],3))