class Solution:
    def maxProduct(self, n: int) -> int:
        n=str(n)
        dig=[]
        for i in n:
            dig.append(int(i))
        dig.sort()
        return dig[-1]*dig[-2]
        