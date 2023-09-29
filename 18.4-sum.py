#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
from typing import List, Tuple


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def nSum(
            n: int,
            left: int,
            right: int,
            target: int,
            curr: List[int],
            result: set[Tuple[int]],
        ):
            if n == 2:
                i, j = left, right - 1
                if target < nums[i] * 2 or target > nums[j] * 2:
                    return
                while i < j:
                    if nums[i] + nums[j] == target:
                        result.add(tuple(curr + [nums[i], nums[j]]))
                        i, j = i + 1, j - 1
                    elif nums[i] + nums[j] < target:
                        i += 1
                    else:
                        j -= 1
            else:
                for i in range(left, right - n + 1):
                    nSum(
                        n - 1, i + 1, right, target - nums[i], curr + [nums[i]], result
                    )

        result = set()
        nSum(4, 0, len(nums), target, [], result)
        return list(result)


# @lc code=end
print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
