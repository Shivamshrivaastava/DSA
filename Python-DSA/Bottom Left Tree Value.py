# Define the TreeNode class for the binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_bottom_left_value(root):
    # Base case: if the root is None, return None
    if root is None:
        return None
    
    # Initialize a queue to perform level order traversal
    queue = [root]
    # Initialize a variable to store the bottom-left value
    bottom_left = None
    
    # Perform level order traversal
    while queue:
        # Get the size of the current level
        size = len(queue)
        # Reset bottom_left for each level
        bottom_left = queue[0].val
        
        # Iterate through all nodes in the current level
        for i in range(size):
            # Pop the front node from the queue
            node = queue.pop(0)
            # Check if the left child exists, if yes, add it to the queue
            if node.left:
                queue.append(node.left)
            # Check if the right child exists, if yes, add it to the queue
            if node.right:
                queue.append(node.right)
    
    # At the end of the loop, bottom_left will store the bottom-left value
    return bottom_left

def main():
    # Create a sample binary tree
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    # Find the bottom-left value
    result = find_bottom_left_value(root)
    print("Bottom Left Value:", result)

if __name__ == "__main__":
    main()
