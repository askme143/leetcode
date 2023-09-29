#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
from collections import deque


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        _map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = deque([])

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not stack or stack.pop() != _map[c]:
                    return False
        return len(stack) == 0


# @lc code=end
print(Solution().isValid("[]"))
