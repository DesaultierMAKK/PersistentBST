from Path_BST import Tree

def test_persistent_bst_path_copying():
    bst = Tree()

    # Insert keys into version 1
    bst_v1 = bst.insert(5).insert(3).insert(7)

    # Search keys in version 1
    assert bst_v1.search(7).key == 7
    assert bst_v1.search(6) is None

    # Insert keys into version 2
    bst_v2 = bst_v1.insert(6)

    # Search keys in version 2
    assert bst_v2.search(6).key == 6
    assert bst_v2.search(7).key == 7

    # Search keys in version 1 again
    assert bst_v1.search(7).key == 7
    assert bst_v1.search(6) is None

    # Delete keys from version 2
    bst_v3 = bst_v2.delete(6).delete(3)

    # Search keys in version 3
    assert bst_v3.search(6) is None
    assert bst_v3.search(3) is None
    assert bst_v3.search(5).key == 5

    print("All tests cases passed")

test_persistent_bst_path_copying()