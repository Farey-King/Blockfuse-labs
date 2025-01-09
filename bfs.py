from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root, result):
    if root is None:
        return None
    search = deque([root])
    while search:
        child = search.popleft()
        if child.value == result:
            return child
        if child.left:
            search.append(child.left)
        if child.right:
            search.append(child.right)
    return None

# An illustration:

root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)

result = 0
outcome = bfs(root, result)
if outcome:
    print(f"Node with value of {result} exist.")
else:
    print(f"Node with value of {result} does not exist.")