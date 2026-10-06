class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    p=stack.pop()
                    if p!=hashmap[c]:
                        return False
        return not stack
        