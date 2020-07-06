from typing import List


class Solution:
    """
    @title 63. 不同路径 II
    @method 动态规划
    """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0]) for _ in obstacleGrid]

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


Solution().uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])