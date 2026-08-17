# from functools import lru_cache

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        """-------this gives us TLE for some reason..----------------"""
        # n = len(stoneValue)
        
        # prefixSum = [0] * (n + 1)
        # for i in range(n):
        #     prefixSum[i + 1] = prefixSum[i] + stoneValue[i]
            
        # def getSum(left, right):
        #     return prefixSum[right + 1] - prefixSum[left]
            
        # @lru_cache(None)
        # def dp(left, right):
        #     if left == right:
        #         return 0
                
        #     maxScore = 0
            
        #     for i in range(left, right):
        #         leftSum = getSum(left, i)
        #         rightSum = getSum(i + 1, right)
                
        #         if leftSum < rightSum:
        #             curScore = leftSum + dp(left, i)
        #             maxScore = max(maxScore, curScore)
                    
        #         elif leftSum > rightSum:
        #             curScore = rightSum + dp(i + 1, right)
        #             maxScore = max(maxScore, curScore)
                    
        #         else:
        #             ifChosenLeft = dp(left, i)
        #             ifChosenRight = dp(i + 1, right)
        #             curScore = leftSum + max(ifChosenLeft, ifChosenRight)
        #             maxScore = max(maxScore, curScore)
                    
        #     return maxScore
            
        # return dp(0, n - 1)

        n = len(stoneValue)
        
        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]

        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]
            
        for left in range(n - 1, -1, -1):
            
            mid = left - 1 
            leftSum = 0
            totalSum = stoneValue[left]
            
            for right in range(left + 1, n):
                totalSum += stoneValue[right]
                
                while mid + 1 < right and (leftSum + stoneValue[mid + 1]) * 2 <= totalSum:
                    mid += 1
                    leftSum += stoneValue[mid]
                    
                res = 0
                
                if mid >= left and leftSum * 2 == totalSum:
                    res = max(maxL[left][mid], maxR[mid + 1][right])
                else:
                    if mid >= left:
                        res = maxL[left][mid]
                    if mid + 1 < right:
                        res = max(res, maxR[mid + 2][right])
                        
                dp[left][right] = res
                
                maxL[left][right] = max(maxL[left][right - 1], totalSum + res)
                maxR[left][right] = max(maxR[left + 1][right], totalSum + res)
                
        return dp[0][n - 1]