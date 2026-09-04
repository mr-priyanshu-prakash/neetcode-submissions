class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

    # 1. Initialize the first window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

    # 2. Slide the window across s2
        for i in range(len(s1), len(s2)):
        # If the counts match, a permutation is found
            if s1_count == window_count:
                return True
        
        # Add the new character entering the window on the right
            window_count[ord(s2[i]) - ord('a')] += 1
        
        # Remove the character leaving the window on the left
            left_char_index = ord(s2[i - len(s1)]) - ord('a')
            window_count[left_char_index] -= 1

    # 3. Check the very last window after the loop finishes
        return s1_count == window_count