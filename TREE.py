#Create a class BINARY TREE that contains background information of product prices (product code, price of 1 product). The tree is sorted by product codes. From the keyboard enter data on the number of products in the format: product code, number of products. Using a tree, find the cost of products (cost = quantity * price of one product).



class Node:
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None;
        
        
root = Node(1);

root.left = Node(2);
root.right = Node(3);

def preorderT(node):
        if node:
            preorderT(node.left);
            
            preorderT(node.right);
            
            print(node.data);
            
preorderT(root);
