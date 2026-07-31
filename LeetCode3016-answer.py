from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:

        ans = 0

        freq = sorted(Counter(word).values(), reverse=True)

        for i in range(len(freq)):

            if i < 8:
                cost = 1

            elif i < 16:
                cost = 2

            elif i < 24:
                cost = 3

            else:
                cost = 4

            ans += freq[i] * cost

        return ans