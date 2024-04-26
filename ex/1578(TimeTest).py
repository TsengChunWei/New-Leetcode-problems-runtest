import os
import sys

currpath = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currpath))

import random
from RuntestPacketge import ListNode, TreeNode
from RuntestPacketge import Tester, SolAlgoTester

class compare:
    def f1(self, colors, neededTime):
        def non_max_sum(array):
            max_num, sum_nums = 0, 0
            for num in array:
                if max_num > num:
                    sum_nums += num
                else:
                    sum_nums += max_num
                    max_num = num
            return sum_nums
        compare_time = [neededTime[0]]
        result = 0
        for i in range(1, len(neededTime)):
            if colors[i-1] == colors[i]:
                compare_time.append(neededTime[i])
            else:
                result += non_max_sum(compare_time)
                compare_time = [neededTime[i]]
        result += non_max_sum(compare_time)
        return result
        
    def f2(self, colors, neededTime):
        max_num = neededTime[0]
        result = sum(neededTime)
        for i in range(1, len(neededTime)):
            if colors[i-1] == colors[i]:
                if max_num < neededTime[i]:
                    max_num = neededTime[i]
            else:
                result -= max_num
                max_num = neededTime[i]
        result -= max_num
        return result
    
    def f3(self, colors, neededTime):
        max_num = neededTime[0]
        result = neededTime[0]
        for i in range(1, len(neededTime)):
            result += neededTime[i]
            if colors[i-1] == colors[i]:
                if max_num < neededTime[i]:
                    max_num = neededTime[i]
            else:
                result -= max_num
                max_num = neededTime[i]
        result -= max_num
        return result


    def SolAlgo(self, colors, neededTime):
        sum_cost = 0
        curr = colors[0]
        max_time = neededTime[0]
        for i in range(1, len(neededTime)):
            if curr == colors[i]:
                if neededTime[i] > max_time:
                    sum_cost += max_time
                    max_time = neededTime[i]
                else:
                    sum_cost += neededTime[i]
            else:
                curr = colors[i]
                max_time = neededTime[i]
        return sum_cost 


"""
Constraints:
● n == colors.length == neededTime.length
● 1 <= n <= 10^5
● 1 <= neededTime[i] <= 10^4
● colors contains only lowercase English letters.
"""
def TestExample(max_length = 10**5, max_time = 10**4):
    en = "abcdefghijklmnopqrstuvwxyz"
    colors = [random.choice(en) for _ in range(max_length)]
    neededTime = [random.randint(1, max_time) for _ in range(max_length)]
    return [colors, neededTime]

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
Tester(Type, "f2", Cp.f2, input, to_, times, sol_answer, False)
Tester(Type, "f3", Cp.f3, input, to_, times, sol_answer, False)