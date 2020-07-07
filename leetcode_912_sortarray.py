from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.insertion_sort(nums)

    @staticmethod
    def selection_sort(nums: List[int]) -> List[int]:
        """
        @method 选择排序

        找到数组中最大元素，存放到起始位置，
        再从剩余元素中找到最大元素，存放到已排序数组的末尾......
        """

        for i in range(len(nums))[:-1]:
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        return nums

    @staticmethod
    def bubble_sort(nums: List[int]) -> List[int]:
        """
        @method 冒泡排序

        比较相邻元素，将大的数慢慢“沉底”(数组尾部)。
        """

        for i in range(len(nums) - 2):
            for j in range(1, len(nums) - i):
                if nums[j] < nums[j - 1]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums

    @staticmethod
    def insertion_sort(nums: List[int]) -> List[int]:
        """
        @method 插入排序

        遍历每一个元素，将它们插入到已排序数组的合适位置中。
        """

        for i in range(1, len(nums)):
            while i > 0 and nums[i] < nums[i - 1]:
                nums[i], nums[i - 1], i = nums[i - 1], nums[i], i - 1
        return nums


array = Solution.insertion_sort([2,5,1,23,12,7,43])
print(array)

