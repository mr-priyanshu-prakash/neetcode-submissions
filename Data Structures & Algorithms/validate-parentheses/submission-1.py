class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map each closing bracket to its matching opening bracket
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the topmost element from the stack if it exists, otherwise assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the expected opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched. If not, it's invalid.
        return not stack
        