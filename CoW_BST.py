class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class PersistentBST:
    def __init__(self):
        self.roots = []  # array to store root nodes of each version
    
    # Search 
    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def search_version(self, version, key):
        if version < len(self.roots):
            return self._search(self.roots[version], key)
        else:
            return None

    def _copy_node(self, node):
        if node is None:
            return None
        return Node(node.key, self._copy_node(node.left), self._copy_node(node.right))

    # Insert
    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            return Node(root.key, self._insert(root.left, key), root.right)
        elif key > root.key:
            return Node(root.key, root.left, self._insert(root.right, key))
        else:  # key already exists
            return root

    def insert_version(self, version, key):
        # Ensure the array is large enough to accommodate the new version
        if len(self.roots) <= version:
            self.roots.extend([None] * (version - len(self.roots) + 1))
        # Create a new root node by copying the previous version's root
        new_root = self._insert(self.roots[version - 1], key) if version > 0 else Node(key)
        self.roots[version] = new_root

    # Delete
    def _delete(self, root, key):
        if root is None:
            return None
        if key < root.key:
            return Node(root.key, self._delete(root.left, key), root.right)
        elif key > root.key:
            return Node(root.key, root.left, self._delete(root.right, key))
        else:  # Found the node to delete
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:  # Node has two children
                # Find the inorder successor (smallest node in the right subtree)
                successor = root.right
                while successor.left:
                    successor = successor.left
                # Replace the key of the node to be deleted with the key of the successor
                root.key = successor.key
                # Delete the successor node from the right subtree
                root.right = self._delete(root.right, successor.key)
            return root

    def delete_version(self, version, key):
        # Ensure the version exists
        if version < len(self.roots):
            # Create a new root node by copying the previous version's root
            new_root = self._delete(self.roots[version], key)
            self.roots[version] = new_root

# Example
bst = PersistentBST()
bst.insert_version(1, 5)
bst.insert_version(1, 3)
bst.insert_version(1, 7)

bst.insert_version(2, 5)
bst.insert_version(2, 3)
bst.insert_version(2, 7)
bst.insert_version(2, 6)

print("Version 1:")
print(bst.search_version(1, 7))  # Output: Node object with key 7
print(bst.search_version(1, 6))  # Output: None (6 not in version 1)

print("Version 2:")
print(bst.search_version(2, 7))  # Output: Node object with key 7
print(bst.search_version(2, 6))  # Output: Node object with key 6

# Delete a node in version 2
bst.delete_version(2, 6)
print("After deletion in version 2:")
print(bst.search_version(2, 6))  # Output: None (6 is deleted in version 2)
