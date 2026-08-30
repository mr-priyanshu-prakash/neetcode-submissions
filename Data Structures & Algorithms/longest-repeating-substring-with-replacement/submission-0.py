class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        max_length = 0

        for right in range(len(s)):
        # Add the current character to the frequency map
            count[s[right]] = count.get(s[right], 0) + 1
        
        # Update the highest frequency seen in the current window
            max_freq = max(max_freq, count[s[right]])

        # If the window is invalid, shrink it from the left
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

        # Update the maximum valid window length
            max_length = max(max_length, right - left + 1)

        return max_length