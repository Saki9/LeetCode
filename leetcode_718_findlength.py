from typing import List


class Solution:
    """
    @title 718. 最长重复子数组
    @method 动态规划

    [[0, 0, 1, 0, 0],
    [0, 1, 0, 2, 0],
    [1, 0, 0, 0, 3],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
    """

    def findLength(self, A: List[int], B: List[int]) -> int:
        dp, res = [[0] * len(A) for _ in range(len(B))], 0
        for i in range(len(A)):
            for j in range(len(B)):
                if B[j] == A[i]:
                    dp[j][i] = dp[j - 1][i - 1] + 1 if j - 1 >= 0 and i - 1 >= 0 else 1
                    res = max(res, dp[j][i])
        return res

print(Solution().findLength([1,2,3,2,1],[3,2,1,4,7]))