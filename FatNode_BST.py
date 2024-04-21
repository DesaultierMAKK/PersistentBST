class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.versions = [(key, value)]

class PersistentBST:
    def __init__(self):
        self.root = None
    # Insert
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        elif key < node.key:
            new_left = self._insert(node.left, key, value)
            new_node = Node(node.key, node.value, left=new_left, right=node.right)
            new_node.versions = node.versions  # Assign versions to the new node
            return new_node
        elif key > node.key:
            new_right = self._insert(node.right, key, value)
            new_node = Node(node.key, node.value, left=node.left, right=new_right)
            new_node.versions = node.versions  # Assign versions to the new node
            return new_node
        else:
            # Key already exists, update value
            node.value = value
            node.versions.append((key, value))
            return node

    # Search
    def search(self, key, version=None):
        return self._search(self.root, key, version)

    def _search(self, node, key, version):
        if node is None:
            return None
        elif key == node.key:
            if version is None:
                return node.value
            else:
                for k, v in node.versions:
                    if k == version:
                        return v
                return None
        elif key < node.key:
            return self._search(node.left, key, version)
        else:
            return self._search(node.right, key, version)



# Example usage:
bst = PersistentBST()
bst.insert(5, 'five')
bst.insert(3, 'three')
bst.insert(7, 'seven')

# Version 1
print(bst.search(5))  # Output: 'five'
print(bst.search(3))  # Output: 'three'
print(bst.search(7))  # Output: 'seven'

# Version 2
bst.insert(5, 'five-updated')
print(bst.search(5))  # Output: 'five-updated'

# Version 3
print(bst.search(5, version=2))  # Output: 'five'
