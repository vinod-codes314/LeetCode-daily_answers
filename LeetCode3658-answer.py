class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oc=ec=0
        for i in range(1,n*2+1):
            if i%2==0:
                ec+=i
            else:
                oc+=i
        return math.gcd(oc,ec)
        