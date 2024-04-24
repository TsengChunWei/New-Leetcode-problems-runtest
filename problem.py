# ● 

# Description
"""

"""

# Code
import os
import sys

currpath = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currpath))

from Runtest import ListNode, TreeNode
from Runtest import Submisstions

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
    def SolAlgo(self, head):
        fast = slow = head
        length = 0
        while fast:
            fast = fast.next
            length += 1
        half = length //2
        while half > 0:
            slow = slow.next
            half -= 1
        return slow
    
# Submisstions
inputs = ["head"]
to_ = [0]
Sol = Solution()
Tc = Testcase()

# data_structure: "", "linklist", "treenode"
# Submisstions(data_structure, inputstr, to_, algorithm, Cases, Expected, SolAlgo, RightSolAlgo, output_type_transform)
Submisstions("linklist", inputs, to_, Sol.middleNode, Tc.Case, Tc.Expected, Tc.SolAlgo, True, True)
