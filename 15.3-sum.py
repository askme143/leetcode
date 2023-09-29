#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        length = len(nums)
        nums.sort()
        for i in range(length):
            j = i + 1
            k = length - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ret.add((nums[i], nums[j], nums[k]))
                    j, k = j + 1, k - 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return list(ret)


# @lc code=end

print(Solution().threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
