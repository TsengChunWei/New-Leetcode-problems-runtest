# ● 

# Description
"""

"""

# Code
import os
import sys

currpath = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currpath))

from RuntestPacketge import classSubmisstions

from typing import List, Optional


class ClassName:
    def __init__(self) -> None:
        self.null = None
    def function1(self) -> type:
        return
    
# Testcase
class Testcase:
    Case = [
        [
            ["ClassName", "function1"], 
            [[], []]
        ]
    ]
    Expected = [
        [None, None]
    ]

class SolClass:
    def __init__(self) -> None:
        self.null = None
    def function1(self) -> type:
        return
    

# Submisstions
def RunClass(cls, operation, content):
    solution = [None]
    for model, value in zip(operation[1:], content[1:]):
        if model == "function1":
            sol = cls.function1()
    return solution
def main(RightSol):
    CN = ClassName()
    SLCL = SolClass()
    Tc = Testcase()
    classSubmisstions(RunClass, CN, Tc.Case, Tc.Expected, SLCL, RightSol)

if __name__ == "__main__":
    RightSol = False
    main(RightSol)