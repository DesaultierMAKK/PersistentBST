class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root
    
    # Search
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    # Insert
    def insert(self, key):
        new_root = self._insert_recursive(self.root, key)
        return Tree(new_root)
    
    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            new_left = self._insert_recursive(node.left, key)
            return Node(node.key, new_left, node.right)
        elif key > node.key:
            new_right = self._insert_recursive(node.right, key)
            return Node(node.key, node.left, new_right)
        else:
            return node  # Key already exists, no need to modify
    
    # Delete
    def delete(self, key):
        new_root = self._delete_recursive(self.root, key)
        return Tree(new_root)
    
    def _delete_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            new_left = self._delete_recursive(node.left, key)
            return Node(node.key, new_left, node.right)
        elif key > node.key:
            new_right = self._delete_recursive(node.right, key)
            return Node(node.key, node.left, new_right)
        else:
            # Key found, delete it
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Node has two children
                successor = self._find_min(node.right)
                new_right = self._delete_recursive(node.right, successor.key)
                return Node(successor.key, node.left, new_right)
    
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def view(self):
    # Visualization of the tree structure using an iterative approach
        if self.root is None:
            print("Tree is empty")
            return

        # Stack to keep track of nodes and their depth
        stack = [(self.root, 0)]
        
        while stack:
            node, depth = stack.pop()
            
            # Print the current node with indentation based on its depth
            print(" " * depth * 4 + f"-> {node.key}")
            
            # Add children to the stack (right child first to print left child first)
            if node.right is not None:
                print("Right")
                stack.append((node.right, depth + 1))
                
            if node.left is not None:
                print("Left")
                stack.append((node.left, depth + 1))


#### INORDER TRAVERSAL
def printInorder(node):
    if node is None:
        return
 
    # First recur on left subtree
    printInorder(node.left)
 
    # Now deal with the node
    print(node.key, end=' ')
 
    # Then recur on right subtree
    printInorder(node.right)

#### Visualizing the tree
#Initialize an empty tree
tree = Tree()

# Perform insertions and keep track of tree versions
tree1 = tree.insert(5)
print("Tree Version 1:")
#tree1.view()
#printInorder(tree1.root)
print()

tree2 = tree1.insert(3)
print("Tree Version 2:")
#tree2.view()
printInorder(tree2.root)
print()

tree3 = tree2.insert(7)
print("Tree Version 3:")
printInorder(tree3.root)
#tree3.view()
print()

tree4 = tree3.insert(4)
print("Tree Version 4:")
printInorder(tree4.root)
#tree4.view()
print()

tree5 = tree4.insert(6)
print("Tree Version 5:")
printInorder(tree5.root)
#tree5.view()
print()

# Perform deletion and keep track of the new version
tree6 = tree5.delete(3)
print("Tree Version 6 (After deleting key 3):")
#tree6.view()
printInorder(tree6.root)
print()