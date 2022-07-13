from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([0,4,5,0,3,6]))