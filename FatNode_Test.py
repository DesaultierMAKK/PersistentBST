from FatNode_BST import PersistentBST
def test_persistent_bst():
    bst = PersistentBST()

    # Insert some nodes
    bst.insert(5, 'five')
    bst.insert(3, 'three')
    bst.insert(7, 'seven')

    # Version 1
    assert bst.search(5) == 'five'
    assert bst.search(3) == 'three'
    assert bst.search(7) == 'seven'

    # Version 2
    bst.insert(5, 'five-updated')
    assert bst.search(5) == 'five-updated'

    # Test searching for non-existent key
    assert bst.search(10) is None

    print("All tests passed!")

if __name__ == "__main__":
    test_persistent_bst()


