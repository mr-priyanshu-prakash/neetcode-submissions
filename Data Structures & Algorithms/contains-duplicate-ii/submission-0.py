class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sett=set()
        l=0
        for r in range(len(nums)):
            if r-l>k:
                sett.remove(nums[l])
                l+=1
            if nums[r] in sett:
                return True
            sett.add(nums[r])
        return False