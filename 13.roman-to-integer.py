#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        _map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        last_int = 1000
        ret = 0

        for c in s:
            curr = _map[c]
            if last_int < curr:
                ret = ret - last_int * 2
            ret += curr
            last_int = curr

        return ret


# @lc code=end
