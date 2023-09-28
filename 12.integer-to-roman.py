#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        m_count = num // 1000
        c_count = (num % 1000) // 100
        x_count = (num % 100) // 10
        i_count = num % 10

        m_str = "M" * m_count
        c_str = (
            "CM"
            if c_count == 9
            else "CD"
            if c_count == 4
            else "D" + "C" * (c_count - 5)
            if c_count >= 5
            else "C" * c_count
        )
        x_str = (
            "XC"
            if x_count == 9
            else "XL"
            if x_count == 4
            else "L" + "X" * (x_count - 5)
            if x_count >= 5
            else "X" * x_count
        )
        i_str = (
            "IX"
            if i_count == 9
            else "IV"
            if i_count == 4
            else "V" + "I" * (i_count - 5)
            if i_count >= 5
            else "I" * i_count
        )

        return m_str + c_str + x_str + i_str


# @lc code=end
