class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        kl=[]
        n=0
        for i in range(len(nums)+1):
            kl.append(n+k)
            n=n+k
        
        for i in range(len(kl)):
            if kl[i] not in nums:
                return kl[i]
        