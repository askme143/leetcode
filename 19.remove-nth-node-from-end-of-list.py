#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def traverse(node: Optional[ListNode]) -> (Optional[ListNode], int):
            if node == None:
                return (None, 0)
            next_node, nth = traverse(node.next)
            node.next = next_node

            if nth + 1 == n:
                return (node.next, nth + 1)
            else:
                return (node, nth + 1)

        tmp_node = ListNode(0, head)
        traverse(tmp_node)
        return tmp_node.next


# @lc code=end
print(Solution().removeNthFromEnd(head=ListNode(1, None), n=1))
