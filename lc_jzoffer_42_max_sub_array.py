from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        """
        剑指 Offer 42. 连续子数组的最大和
        解法：动态规划
        :param nums:
        :return:
        """
        dp = nums[:]
        for i in range(len(nums))[1:]:
            if nums[i] + dp[i - 1] > nums[i]: dp[i] = nums[i] + dp[i - 1]
        return max(dp)


print(Solution().max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))