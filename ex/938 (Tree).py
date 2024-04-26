# 938. Range Sum of BST

# Description
"""
https://leetcode.com/problems/range-sum-of-bst/description/

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


Example 1:
    https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg
    |       10
    |     ／  ＼　
    |    5     15
    |  ／ ＼　   ＼
    | 3    7      18
    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32
    Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
    https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg
    |           10
    |        ／    ＼
    |       5       15
    |     ／ ＼    ／  ＼
    |    3    7  13     18
    |  ／    ／ 
    | 1 `   6
    Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    Output: 23
    Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
    

Constraints:
● The number of nodes in the tree is in the range [1, 2 * 10^4].
● 1 <= Node.val <= 10^5
● 1 <= low <= high <= 10^5
● All Node.val are unique.
"""

# Code
import os
import sys

currpath = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currpath))

from RuntestPacketge import ListNode, TreeNode
from RuntestPacketge import Submisstions

from typing import List, Optional


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        if root is None:
            return 0
        if root.val < low:
            result += self.rangeSumBST(root.right, low, high)
        elif low <= root.val and root.val <= high:
            result += root.val
            result += self.rangeSumBST(root.left, low, high)
            result += self.rangeSumBST(root.right, low, high)
        elif high < root.val:
            result += self.rangeSumBST(root.left, low, high)

        return result

# Testcase
class Testcase:
    Case = [
        [[10,5,15,3,7,None,18], 7, 15],
        [[10,5,15,3,7,13,18,1,None,6], 6, 10],
        [[10,5,15,4,6,14,16], 6, 15]
    ]

    Expected = [
        32,
        23,
        45
    ]
    def SolAlgo(self, root, low, high):
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if node and low <= node.val <= high:
                ans += node.val
            if node and low< node.val:
                stack.append(node.left)
            if node and node.val< high:
                stack.append(node.right)
        return ans
    

# Submisstions
def main(Type, inputs, to_, RightSol, output_type_transform):
    Sol = Solution()
    Tc = Testcase()
    Submisstions(Type, inputs, to_, Sol.rangeSumBST, Tc.Case, Tc.Expected, Tc.SolAlgo, RightSol, output_type_transform)

if __name__ == "__main__":
    # "", "linklist", "treenode"
    Type = "treenode"  

    inputs = ["root", "low", "high"]
    to_ = [0]
    RightSol = True
    output_type_transform = False
    main(Type, inputs, to_, RightSol, output_type_transform)