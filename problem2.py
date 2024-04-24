# ● 

# Description
"""

"""

# Code
import heapq
from typing import List, Optional
import os
import sys

currpath = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currpath))

from Runtest import ListNode, TreeNode
from Runtest import Submisstions, classSubmisstions


class Solution:
    def __init__(self):
        self.min = 1
        self.add = []
        
    def popSmallest(self) -> int:
        if self.add:
            return self.add.pop(0)
        self.min += 1
        return self.min-1
        
    def addBack(self, num: int) -> None:
        if num < self.min and num not in self.add:
            self.add.append(num)
            self.add.sort()
        return None


# Testcase
class Testcase:
    Case = [
        [
            ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"],
            [[], [2], [], [], [], [1], [], [], []]
        ]
    ]

    Expected = [
        [None, None, 1, 2, 3, None, 1, 4, 5]
    ]

class SolClass():
    def __init__(self):
        self.cur_integer = 1
        self.added = []
        self.present = set()

    def popSmallest(self) -> int:
        if self.added:
            answer = heapq.heappop(self.added)
            self.present.remove(answer)
        else:
            answer = self.cur_integer
            self.cur_integer += 1
        return answer

    def addBack(self, num: int) -> None:
        if num >= self.cur_integer or num in self.present:
            return
        heapq.heappush(self.added, num)
        self.present.add(num)
    
# Submisstions
inputs = ["SmallestInfiniteSet", "popSmallest", "addBack"]
to_ = []
Sol = Solution()
Tc = Testcase()
Type = "class"  # "", "linklist", "treenode". "class"

def RunClass(cls, operation, content):
    solution = [None]
    for model, value in zip(operation[1:], content[1:]):
        if model == "addBack":
            sol = cls.addBack(value[0])
        elif model == "popSmallest":
            sol = cls.popSmallest()
        solution.append(sol)
    return solution

if Type == "class":
    # classSubmisstions(RunClass, className, Cases, Expected, SolClass, RightSolClass)
    classSubmisstions(RunClass, Sol, Tc.Case, Tc.Expected, SolClass(), True)
else:
    # Submisstions(data_structure, inputstr, to_, algorithm, Cases, Expected, SolAlgo, RightSolAlgo, output_type_transform)
    Submisstions("class", inputs, to_, None, Tc.Case, Tc.Expected, None, False, False)
