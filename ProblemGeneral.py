# ● 

# Description
"""

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
    def Algorithm(self, input: type) -> type:
        return 

# Testcase
class Testcase:
    Case = [
        [0],
    ]
    Expected = [
        0
    ]
    def SolAlgo(self, input):
        return
    

# Submisstions
def main(Type, inputs, to_, RightSol, output_type_transform):
    Sol = Solution()
    Tc = Testcase()
    Submisstions(Type, inputs, to_, Sol.Algorithm, Tc.Case, Tc.Expected, Tc.SolAlgo, RightSol, output_type_transform)

if __name__ == "__main__":
    # "", "linklist", "treenode". "class"
    Type = ""  

    inputs = [""]
    to_ = []
    RightSol = False
    output_type_transform = False
    main(Type, inputs, to_, RightSol, output_type_transform)

