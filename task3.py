from task1 import Node, insert

def sum_tree(root):
    if root is None:
        return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)

if __name__ == "__main__":
    root = None
    for value in [10, 95, 60, 40, 5, 150, 370]:
        root = insert(root, value)

    print("Сума всіх значень у дереві:", sum_tree(root))
