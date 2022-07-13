from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        for i in range((len(prices))-1):
            if prices[i]<prices[i+1]:
                sum += prices[i+1]-prices[i]
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))