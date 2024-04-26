import heapq
import os
import sys

currpath = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currpath))

import random
from RuntestPacketge import ListNode, TreeNode
from RuntestPacketge import classTester, SolClassTester

class class1:
    def __init__(self) -> None:
        self.null = None
    def function1(self) -> type:
        return

    

class SolClass():
    def __init__(self) -> None:
        self.null = None
    def function1(self) -> type:
        return


def RunClass(cls, ModelValue):
    Ans = [None]
    for model, value in zip(ModelValue[0][1:], ModelValue[1][1:]):
        if model == "function1":
            sol = cls.function1()
        Ans.append(sol)
    return Ans

def TestExample(max_num = 1000):
    length = max_num
    Model = ["Class"]*length
    Value = [[]]*length
    for i in range(1, length):
        r = 0
        if r == 0:
            Model[i] = "function1"
    ModelValue = [Model, Value]
    return ModelValue

# ================================
# ================================
# ================================
times = 10
input = TestExample()

print("\nThe Efficiency Comparison of Various Algorithms through Time Testing :\n")
sol_answer = SolClassTester(RunClass, SolClass(), input, times)
classTester("class1", RunClass, class1(), input, times, sol_answer)