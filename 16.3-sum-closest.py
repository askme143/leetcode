#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)

        delta_min = nums[0] + nums[1] + nums[-1] - target
        for i in range(length):
            if delta_min == 0:
                break

            j, k = i + 1, length - 1
            while j < k:
                delta = nums[i] + nums[j] + nums[k] - target
                if abs(delta) < abs(delta_min):
                    delta_min = delta
                if delta == 0:
                    break
                elif delta < 0:
                    j += 1
                else:
                    k -= 1
        return target + delta_min


# @lc code=end
