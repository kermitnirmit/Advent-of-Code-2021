import ast
import math

f = open("input.txt").read().strip().split("\n")
rsum = ast.literal_eval(f[0])


def getPathToFirstLevel4(node):
    queue = [(node, 0, "", None)]
    while queue:
        n, l, p, parent = queue.pop(0)
        if l == 5:
            return n, p
        if n.l is not None:
            queue.append((n.l, l + 1, p + "L", n))
        if n.r is not None:
            queue.append((n.r, l + 1, p + "R", n))
    return None, None


def getPathToFirst10plus(node):
    queue = [(node, "", None)]
    while queue:
        # print(queue)
        n, p, parent = queue.pop(-1)
        if n.val is not None and n.val > 9:
            # print("found a 10 plus", n, p)
            return n, p
        if n.r is not None:
            queue.append((n.r, p + "R", n))
        if n.l is not None:
            queue.append((n.l, p + "L", n))
    return None, None


class Node:
    def __init__(self, l=None, r=None, val=None):
        self.l = l
        self.r = r
        self.val = val

    def __add__(self, other):
        parent = Node(self, other)
        parent.afterAddition()
        return parent

    def afterAddition(self):
        while True:
            node, path = getPathToFirstLevel4(self)
            if node is not None:
                path = path[:-1]  # this gets to one of the points inside it i dont need that, i need the parent
                n, p = self.followPath(path)  # this gets to the node dictated by a path
                pred, parent = self.getPredessor(path)
                succ, succParent = self.getSuccessor(path)
                if succ:
                    succ.val += n.r.val
                if pred:
                    pred.val += n.l.val
                n.l = None
                n.r = None
                n.val = 0
                continue
            ng10, pg10 = getPathToFirst10plus(self)
            if ng10 is not None:
                n, p = self.followPath(pg10)
                newNode = Node(None, None, n.val // 2)
                newNodeR = Node(None, None, int(math.ceil(n.val / 2)))
                if p.l == n:
                    p.l = Node(newNode, newNodeR)
                else:
                    p.r = Node(newNode, newNodeR)
                continue
            if node is None and ng10 is None:
                break

    def followPath(self, path):
        i = 0
        parent = None
        curr = self
        while i < len(path) and curr.l is not None and curr.r is not None:
            if path[i] == "L":
                parent = curr
                curr = curr.l
            else:
                parent = curr
                curr = curr.r
            i += 1
        return curr, parent

    def getPredessor(self, path):
        if "R" not in path:
            return None, None
        # r is somewhere in the path, so switch the last one to an L
        i = path.rindex("R")
        newstr = path[:i] + "L"
        # print("finding pred", path, newstr)
        return self.followPathAndKeepGoing(newstr, "R")
        # the pred of a path

    def followPathAndKeepGoing(self, path, dir):
        # print(path)
        curr = self
        parent = None
        i = 0
        while curr.l is not None and curr.r is not None:
            # print(curr)
            if i < len(path):
                if path[i] == "L":
                    parent = curr
                    curr = curr.l
                else:
                    parent = curr
                    curr = curr.r
                i += 1
            else:
                if dir == "L":
                    parent = curr
                    curr = curr.l
                else:
                    parent = curr
                    curr = curr.r
        # print(curr, parent)
        return curr, parent

    def getSuccessor(self, path):
        if "L" not in path:
            return None, None
        # l is somewhere in the path, so switch the last one to an R
        i = path.rindex("L")
        newstr = path[:i] + "R"
        # print("getting successor", path, newstr)
        return self.followPathAndKeepGoing(newstr, "L")

    def __str__(self):
        if self.l is None and self.r is None:
            return str(self.val)
        else:
            return "[" + str(self.l) + ", " + str(self.r) + "]"
        # return "val" + str(self.val) + str(self.l) + str(self.r)

    def magnitude(self):
        if self.val is not None:
            return self.val
        else:
            return self.l.magnitude() * 3 + self.r.magnitude() * 2

def turn_into(root, nested_list):
    if isinstance(nested_list, int):
        root.val = int(nested_list)
        return root
    if isinstance(nested_list, list):
        if nested_list[1] != None:
            root.r = turn_into(Node(), nested_list[1])
        if nested_list[0] != None:
            root.l = turn_into(Node(), nested_list[0])
    return root


rsum = turn_into(Node(), rsum)
for i in range(1, len(f)):
    nextLine = turn_into(Node(), ast.literal_eval(f[i]))
    rsum = rsum + nextLine
print(rsum.magnitude())

q = -1000
for i in range(len(f)):
    for j in range(len(f)):
        if i != j:
            w = turn_into(Node(), ast.literal_eval(f[i]))
            r = turn_into(Node(), ast.literal_eval(f[j]))
            tot = w + r
            q = max(tot.magnitude(), q)
print(q)

