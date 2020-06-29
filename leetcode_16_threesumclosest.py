from typing import List


class Solution:
    """
    @title 16. 最接近的三数之和
    @method 双指针

    @desc 排序 nums，遍历 nums 的每一个元素 nums[i]，
    使头指针指向 i + 1，尾指针指向 len(nums) - 1，
    根据三个元素的和与 target 比较的结果动态调整双指针，
    最终返回过程中记录的最接近 target 的三数之和。
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums, result = sorted(nums), nums[0] + nums[1] + nums[-1]

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


print(Solution().threeSumClosest([-1,2,1,0,0,0,0], 0))