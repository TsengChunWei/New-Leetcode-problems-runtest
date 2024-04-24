import os
import sys

currpath = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currpath))

import random
from Runtest import ListNode, TreeNode
from Runtest import Tester, SolAlgoTester

class compare:
    def f1(self, head):
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n += 1
        for _ in range(n//2):
            head = head.next
        return head
    
    def f2(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
            

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


def TestExample(max_length = 100):
    inputInList = [i+1 for i in range(max_length)]
    return [inputInList]

# ================================
# ================================
# ================================
times = 2048
input = TestExample()
to_ = [0]
Cp = compare()
Type = "linklist"

print("\nThe Efficiency Comparison of Various Algorithms through Time Testing :\n")
sol_answer = SolAlgoTester(Type, Cp.SolAlgo, input, to_, times, True)
Tester(Type, "f1", Cp.f1, input, to_, times, sol_answer, True)
Tester(Type, "f2", Cp.f2, input, to_, times, sol_answer, True)