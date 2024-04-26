# 876. Middle of the Linked List

# Description
"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.


Example 1:
    https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg
    |  1 -→ 2 -→ 3 -→ 4 -→ 5
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

Example 2:
    https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg
    |  1 -→ 2 -→ 3 -→ 4 -→ 5 -→ 6
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
    

Constraints:
● The number of nodes in the list is in the range [1, 100].
● 1 <= Node.val <= 100
"""

# Code
import os
import sys

currpath = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currpath))

from RuntestPacketge import ListNode, TreeNode
from RuntestPacketge import Submisstions, classSubmisstions

from typing import List, Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n += 1
        for _ in range(n//2):
            head = head.next
        return head

# Testcase
class Testcase:
    Case = [
        [[1,2,3,4,5]],
        [[1,2,3,4,5,6]],
        [[1,3,5,7,8,11]]
    ]
    Expected = [
        [3,4,5],
        [4,5,6],
        [7,8,11]
    ]
    def SolAlgo(self, input):
        return
    

# Submisstions
def main(Type, inputs, to_, RightSol, output_type_transform):
    Sol = Solution()
    Tc = Testcase()
    Submisstions(Type, inputs, to_, Sol.middleNode, Tc.Case, Tc.Expected, Tc.SolAlgo, RightSol, output_type_transform)

if __name__ == "__main__":
    # "", "linklist", "treenode"
    Type = "linklist"  

    inputs = ["head"]
    to_ = [0]
    RightSol = False
    output_type_transform = True
    main(Type, inputs, to_, RightSol, output_type_transform)