class Node:
    def __init__(self, data, result):
        self.data = data;
        self.result = result;
        self.left = None;
        self.right = None;
        
root = Node(2, 100);

root.left = Node(1, 101);

root.right = Node(3, 102);
root.right.right = Node(4, 103);

def search(node, value):
    if node != None:
        if node.data == value:
            print("done", node.result);
        if value < node.data:
            search(node.left, value);
        if value > node.data:
            search(node.right, value);
    else:
        print("Search unsuccessful");
        
search(root, 4);
