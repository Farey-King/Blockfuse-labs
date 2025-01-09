class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(root, result):
    if root is None:
        return None
    
    # performing a Search in the left subtree
    left_search = dfs(root.left, result)
    if left_search is not None:
        return left_search
    
    # performing a Search in the right subtree
    right_search = dfs(root.right, result)
    if right_search is not None:
        return right_search


# An illustration:

root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)

result = 3
outcome = dfs(root, result)
if outcome:
    print(f"Node with value of {result} exist.")
else:
    print(f"Node with value of {result} does not exist.")