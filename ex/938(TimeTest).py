import os
import sys

currpath = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currpath))

import random
from RuntestPacketge import ListNode, TreeNode
from RuntestPacketge import Tester, SolAlgoTester

class compare:
    def f1(self, root, low, high):
        result = 0
        if root is None:
            return 0
        if root.val < low:
            result += self.f1(root.right, low, high)
        elif low <= root.val and root.val <= high:
            result += root.val
            result += self.f1(root.left, low, high)
            result += self.f1(root.right, low, high)
        elif high < root.val:
            result += self.f1(root.left, low, high)
        return result
    
    def f2(self, root, low, high):
        if root is None:
            return 0
        result = 0
        if low <= root.val <= high:
            result += root.val
        if root.val > low:
            result += self.f2(root.left, low, high)
        if root.val < high:
            result += self.f2(root.right, low, high)
        return result
    

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

"""
Constraints:
● A binary search tree
● The number of nodes in the tree is in the range [1, 2 * 10^4].
● 1 <= Node.val <= 10^5
● 1 <= low <= high <= 10^5
● All Node.val are unique.
"""
def TestExample(max_length = 2*10**4):
    # 2^16 < 10**5 and 2**17 > 10**5
    # 2^16 + 2^15 + 2^14 + ... + 2 + 1 = 2^17-1 > 2*10^4
    k = 16
    n = 2**k
    array = [2*i+1 for i in range(n)]
    arr = array
    for _ in range(k):
        arr = [(arr[i]+arr[i+1])//2 for i in range(0, n, 2)]
        array = arr + array
        n //= 2
    inputInList = array[:max_length]
    low = 1
    high = inputInList[-1]
    return [inputInList, low, high]

# ================================
# ================================
# ================================
times = 8
input = TestExample()
to_ = [0]
Cp = compare()
# "", "linklist", "treenode". "class"
Type = "treenode"

print("\nThe Efficiency Comparison of Various Algorithms through Time Testing :\n")
sol_answer = SolAlgoTester(Type, Cp.SolAlgo, input, to_, times, False)
Tester(Type, "f1", Cp.f1, input, to_, times, sol_answer, False)
Tester(Type, "f2", Cp.f2, input, to_, times, sol_answer, False)