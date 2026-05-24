

class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)
        t = [-1] * n

        def solve(i):
            if t[i] != -1:
                return t[i]

            result = 1  # count current index also

            # move left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                # can't jump further once taller/equal element appears
                if arr[j] >= arr[i]:
                    break

                result = max(result, 1 + solve(j))

            # move right
            for j in range(i + 1, min(n, i + d + 1)):
                # can't jump further once taller/equal element appears
                if arr[j] >= arr[i]:
                    break

                result = max(result, 1 + solve(j))

            t[i] = result
            return result

        maxJump = 1

        for i in range(n):
            maxJump = max(maxJump, solve(i))

        return maxJump