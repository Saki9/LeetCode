from typing import List


class Solution:
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        """
        16. 最接近的三数之和
        解法：双指针
        :param nums:
        :param target:
        :return:
        """
        nums, result = self.sort_list(nums), nums[0] + nums[1] + nums[-1]

        for i in range(len(nums))[:-2]:
            start, end = i + 1, len(nums) - 1

            while start < end:
                total = nums[i] + nums[start] + nums[end]

                # 根据结果的大小移动指针
                if total == target: return total
                elif total < target: start = start + 1
                elif total > target: end = end - 1

                if abs(total - target) < abs(result - target):
                    result = total

        return result

    @staticmethod
    def sort_list(nums: List[int]) -> List[int]:
        """
        从小到大排序
        :param nums:
        :return:
        """
        for i in range(len(nums))[:-1]:
            for j in range(len(nums))[i:]:
                if nums[j] < nums[i]:
                    cache = nums[i]
                    nums[i], nums[j] = nums[j], cache

        return nums


print(Solution().three_sum_closest([-1,2,1,0,0,0,0], 0))