from CoW_BST import PersistentBST

def test_delete_version():
    # Create a persistent BST
    bst = PersistentBST()

    # Insert nodes into version 1
    bst.insert_version(1, 5)
    bst.insert_version(1, 3)
    bst.insert_version(1, 7)

    # Insert nodes into version 2
    bst.insert_version(2, 5)
    bst.insert_version(2, 3)
    bst.insert_version(2, 7)
    bst.insert_version(2, 6)

    # Delete a node in version 2
    bst.delete_version(2, 6)

    # Test search after deletion
    assert bst.search_version(2, 6) is None, "Node 6 should be deleted in version 2"
    assert bst.search_version(2, 7) is not None, "Node 7 should still exist in version 2"

    # Test search in previous version
    assert bst.search_version(1, 6) is None, "Node 6 should not exist in version 1"
    assert bst.search_version(1, 7) is not None, "Node 7 should exist in version 1"

    print("All test cases passed successfully.")

# Run the test case
test_delete_version()

