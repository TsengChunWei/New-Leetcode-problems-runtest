import os
import sys

currpath = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currpath))

import random
from RuntestPacketge import ListNode, TreeNode
from RuntestPacketge import Tester, SolAlgoTester

class compare:
    def f1(self, input):
        return
              

    def SolAlgo(self, input):
        return


def TestExample(max_length = 100):
    input = None
    return [input]

# ================================
# ================================
# ================================
times = 10
input = TestExample()
to_ = []
Cp = compare()
# "", "linklist", "treenode". "class"
Type = ""

print("\nThe Efficiency Comparison of Various Algorithms through Time Testing :\n")
sol_answer = SolAlgoTester(Type, Cp.SolAlgo, input, to_, times, True)
Tester(Type, "f1", Cp.f1, input, to_, times, sol_answer, False)