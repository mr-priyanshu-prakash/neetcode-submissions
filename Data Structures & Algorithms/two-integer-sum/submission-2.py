class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        l=0
        r=len(nums)-1
        t=0
        while l<r:
            t=nums[l]+nums[r]
            if t==target:
                return [l,r]
            if t>target:
                r-=1
            if t<target:
                l+=1
        return []   
        '''
        dic={}
        for i,n in enumerate(nums):
            diff=target-nums[i]
            if diff in dic:
                return [dic[diff],i]
            dic[n]=i

