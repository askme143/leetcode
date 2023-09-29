#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = min(map(lambda s: len(s), strs))
        ret = 0
        while ret < length:
            if len(set(map(lambda s: s[ret], strs))) == 1:
                ret += 1
            else:
                break
        return strs[0][:ret]


# @lc code=end
