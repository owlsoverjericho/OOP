class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class Linked_List:
    def __init__(self):
        self.head = None;
        
linked_list = Linked_List();

#init the firts element of the list:
linked_list.head = Node(1);

second = Node(2);
third = Node(3);
forth = Node(4);

#connecting the nodes:
linked_list.head.next = second;
second.next = third;
third.next = forth;

while linked_list.head != None:
    print(linked_list.head.data);
    linked_list.head = linked_list.head.next;
