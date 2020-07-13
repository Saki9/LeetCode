from typing import List


class Solution:
    """
    @title 350. 两个数组的交集 II
    @method 哈希表

    定义哈希表存储 nums1 每个元素出现的次数，
    遍历 nums2，如果当前元素在 nums1 中出现次数大于 0，
    则将当前元素加入返回列表中，并将哈希表中记录的次数减 1。
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash, result = {}, []
        for i in nums1:
            hash[i] = hash[i] + 1 if i in hash else 1
        for j in nums2:
            if j in hash and hash[j] > 0:
                result.append(j)
                hash[j] = hash[j] - 1
        return result


Solution().intersect(nums1=[4,9,5], nums2=[9,4,9,8,4])