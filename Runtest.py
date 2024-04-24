from collections import deque
import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_listnode(arr):
    if not arr:
        return None
    root = ListNode(arr[0])
    queue = deque([root])
    k = 1
    while k < len(arr):
        currnode = queue.popleft()
        currnode.next = ListNode(arr[k])
        queue.append(currnode.next)
        k += 1
    return root

def list_to_treenode(arr):
    if not arr: return None
    root = TreeNode(arr[0])
    queue = [root]
    k = 1
    while k < len(arr):
        current_node = queue.pop(0)
        if arr[k] is not None:
            current_node.left = TreeNode(arr[k])
            queue.append(current_node.left)
        k += 1
        if k < len(arr) and arr[k] is not None:
            current_node.right = TreeNode(arr[k])
            queue.append(current_node.right)
        k += 1
    return root

def listnode_to_list(output):
    result = []
    current = output
    while current:
        result.append(current.val)
        current = current.next
    return result

def treenode_to_list(output):
    if not output:
        return []
    result = []
    dq = deque([output])
    while dq:
        node = dq.popleft()
        if node:
            result.append(node.val)
            dq.append(node.left)
            dq.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

class type_transform():
    def __init__(self, data_structure) -> None:
        self.data_structure = data_structure
    def data(self, variables, to_):
        if self.data_structure == "linklist":
            temp = []
            for j, c in enumerate(variables):
                if j in to_:
                    c = list_to_listnode(c)
                temp.append(c)
            variables = temp
        if self.data_structure == "treenode":
            temp = []
            for j, c in enumerate(variables):
                if j in to_:
                    c = list_to_treenode(c)
                temp.append(c)
            variables = temp
        return variables
    def output(self, output, output_type_transform):
        if self.data_structure == "linklist" and output_type_transform:
            output = listnode_to_list(output)
        if self.data_structure == "treenode" and output_type_transform:
            output = treenode_to_list(output)
        return output

def Submisstions(data_structure, inputstr, to_, algorithm, Cases, Expected, SolAlgo, RightSolAlgo, output_type_transform):
    T_type = type_transform(data_structure)
    for i, case in enumerate(Cases):
        input = ", ".join("{} = {}".format(var, val) for  var, val in zip(inputstr, case))
        case = T_type.data(case, to_)
        
        solution = algorithm(*case.copy())
        solution = T_type.output(solution, output_type_transform)

        if RightSolAlgo:
            expected = SolAlgo(*case.copy())
            expected = T_type.output(expected, output_type_transform)
        else:
            expected = Expected[i]

        if solution == expected:
            print(f"Case {i+1}:\n  Input : {input}\n  Output: {solution} (expectly)\n")
        else:
            print(f"Case {i+1}:\n  Input : {input}\n  Output: {solution} (wrong)-->\nExpected: {expected}\n")
    print("-"*60)

def classSubmisstions(RunClass, className, Cases, Expected, SolClass, RightSolClass):
    for i, case in enumerate(Cases):
        operation, content = case[0].copy(), case[1].copy()
        input = f"\n  {operation}\n  {content}"
        solution = RunClass(className, operation, content)
        if RightSolClass:
            expected = RunClass(SolClass, operation, content)
        else:
            expected = Expected[i]
        if solution == expected:
            print(f"Case {i+1}:\n  Input : {input}\n\n  Output: {solution} (expectly)\n")
        else:
            print(f"Case {i+1}:\n  Input : {input}\n\n  Output: {solution} (wrong)-->\nExpected: {expected}\n")
    print("-"*60)

def Runtime(func, input, times):
    temp = time.time()
    for _ in range(times):
        _ = func(*input.copy())
    t = 1000*(time.time()-temp)
    t /= times
    ms, mus = int(t), round(1000*(t-int(t)), 3)
    testtime: str
    if ms == 0 and mus < 10:
        testtime = "{} µs".format(mus)
    elif ms == 0 and mus >= 10:
        testtime = "{} µs".format(int(mus))
    else:
        testtime = "{} ms, {} µs".format(ms, int(mus))
    return testtime

def Tester(data_structure, name, algorithm, input, to_, times, sol_answer, output_type_transform):
    T_type = type_transform(data_structure)
    input = T_type.data(input, to_)
    testtime = Runtime(algorithm, input, times)
    answer = algorithm(*input.copy())
    answer = T_type.output(answer, output_type_transform)
    if answer == sol_answer:
        print("{}: (Exactly) {}".format(name, testtime))
    else:
        print("{}: ( Wrong ) {}".format(name, testtime))
    return

def SolAlgoTester(data_structure, algorithm, input, to_, times, output_type_transform):
    T_type = type_transform(data_structure)
    input = T_type.data(input, to_)
    sol_answer = algorithm(*input.copy())
    sol_answer = T_type.output(sol_answer, output_type_transform)
    print(f"Solution: {Runtime(algorithm, input, times)}")
    return sol_answer

