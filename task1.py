from node import Node, insert

def find_max(root):
    if root is None:
        return None
    current = root
    while current.right:
        current = current.right
    return current.key

if __name__ == "__main__":
    root = None
    for value in [10, 95, 60, 40, 5, 150, 370]:
        root = insert(root, value)

    print("Найбільше значення у дереві:", find_max(root))
