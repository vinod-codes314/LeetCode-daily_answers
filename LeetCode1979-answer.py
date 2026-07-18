class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s=1000
        l=0
        for i in range(0,len(nums)):
            if nums[i]>l:
                l=nums[i]
            if nums[i]<s:
                s=nums[i]
        return math.gcd(s,l)
        