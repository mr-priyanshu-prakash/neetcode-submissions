class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        sett=set()
        for r in range(len(nums)):
            if r-l>k:
                sett.remove(nums[l])
                l+=1
            if nums[r] in sett:
                return True
            sett.add(nums[r])
        return False
