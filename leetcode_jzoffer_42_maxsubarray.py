from typing import List


class Solution:
    """
    @title 剑指 Offer 42. 连续子数组的最大和
    @method 动态规划

    @example nums = [-2,1,-3,4,-1,2,1,-5,4]
             dp = [-2,1,-2,4,3,5,6,1,5]

    dp[i] 代表以元素 nums[i] 为结尾的连续子数组最大和,
    若 dp[i - 1] > 0，则 dp[i - 1] 对 dp[i] 产生正贡献，
    使 dp[i] = nums[i] + dp[i - 1],
    最后返回 dp 中的最大值，代表全局最大值。
    """
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        for i in range(len(nums))[1:]:
            if dp[i - 1] > 0: dp[i] = nums[i] + dp[i - 1]
        return max(dp)


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))