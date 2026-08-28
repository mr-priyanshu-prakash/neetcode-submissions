class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        # Stack will store tuples: (start_index, height)
        stack = [] 
        
        for i, h in enumerate(heights):
            start = i
            
            # If the current bar is shorter than the top of the stack,
            # the taller bars can't extend any further to the right.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                
                # Calculate the area for the popped bar
                max_area = max(max_area, height * (i - index))
                
                # The current shorter bar can extend backward to where the taller bar started
                start = index 
                
            stack.append((start, h))
            
        # Clean up any bars remaining in the stack
        # Their right boundary extends to the very end of the array
        n = len(heights)
        for i, h in stack:
            max_area = max(max_area, h * (n - i))
            
        return max_area