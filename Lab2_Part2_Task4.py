class Node:
    def __init__(self, code, price):
        self.code = code;
        self.price = price;
        self.left = None;
        self.right = None;
        
root = Node(28, 101);

root.left = Node(23, 102);

root.left.left = Node(14, 103);
root.left.right = Node(24, 104);

root.left.left.left = Node(12, 105);
root.left.left.right = Node(17, 106);

root.right = Node(33, 107);
root.right.left = Node(32, 108);

root.right.right = Node(59, 109);

root.right.right.left = Node(54, 110);
root.right.right.right = Node(72, 111);

def preorderTraversal(node):
    if node:
        print(node.code);
        preorderTraversal(node.left);
        preorderTraversal(node.right);

def search(tree, code):
    if tree != None:
        if tree.code == code:
            return tree.price;
        if code < tree.code:
            return search(tree.left, code);
        if code > tree.code:
            return search(tree.right, code);
    else:
        return "Not found";
    
print(search(root, 12));
