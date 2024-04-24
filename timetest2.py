import heapq
import os
import sys

currpath = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currpath))

import random
from Runtest import ListNode, TreeNode
from Runtest import Tester, SolAlgoTester

class compare1:
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

    

class SolutionAlgorithm():
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


def TestExample(max_num = 1000):
    length = max_num
    Model = ["Class"]*length
    Value = [[]]*length
    for i in range(1, length):
        k = random.randint(1, max_num)
        r = random.randint(0, 1)
        if r == 0:
            Model[i] = "popSmallest"
        else:
            Model[i] = "addBack"
            Value[i] = [k]
    ModelValue = [Model, Value]
    return ModelValue

# ================================
# ================================
# ================================
times = 2048
input = TestExample()
to_ = [0]
Type = "linklist"

print("\nThe Efficiency Comparison of Various Algorithms through Time Testing :\n")
sol_answer = SolAlgoTester(Type, Cp.SolAlgo, input, to_, times, True)
Tester(Type, "f1", Cp.f1, input, to_, times, sol_answer, True)
Tester(Type, "f2", Cp.f2, input, to_, times, sol_answer, True)