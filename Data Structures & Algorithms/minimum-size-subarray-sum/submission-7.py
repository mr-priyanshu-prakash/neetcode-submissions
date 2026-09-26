class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minl=float('inf')
        summ=0
        l=0
        for r in range(len(nums)):
            summ+=nums[r]
            while summ>=target:
                minl=min(minl,r-l+1)
                summ-=nums[l]
                l+=1
        return minl if minl!=float('inf') else 0