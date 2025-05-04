from task1 import Node, insert

def find_min(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.key

if __name__ == "__main__":
    root = None
    for value in [10, 95, 60, 40, 5, 150, 370]:
        root = insert(root, value)

    print("Найменше значення у дереві:", find_min(root))
