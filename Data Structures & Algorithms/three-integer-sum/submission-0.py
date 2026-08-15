class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # If the lowest possible number is > 0, no numbers can sum to 0
            if nums[i] > 0:
                break
                
            # Skip duplicate elements for the first position to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum > 0:
                    # Sum is too large, decrease it by moving the right pointer left
                    right -= 1
                elif current_sum < 0:
                    # Sum is too small, increase it by moving the left pointer right
                    left += 1
                else:
                    # Match found! Add the triplet to the result list
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers to search for other possible pairs
                    left += 1
                    right -= 1
                    
                    # Skip duplicate elements for the second position
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res