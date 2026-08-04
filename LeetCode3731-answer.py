class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=[]
        for i in range(nums[0],nums[-1]+1):
            if i not in nums:
                n.append(i)
        return n