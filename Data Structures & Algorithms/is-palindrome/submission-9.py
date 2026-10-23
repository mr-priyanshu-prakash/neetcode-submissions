class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev="".join(st.lower() for st in s if st.isalnum())
        return rev==rev[::-1]