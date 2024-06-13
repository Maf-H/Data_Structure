# Date and Time Jun 12 2024 07:09 pm
# @ author : Mesfin Haftu
"""
1. Insert a value at the beginning of the list (method insertAtFront).
2. Insert a value at the end of the list (method insertAtBack).
3. Delete a value from the front of the list (method removeFromFront).
4. Delete a value from the end of the list (method removeFromBack).
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.next_node = None
        
        
class LinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None
    def add_at_front(self, new_node):
        if self.first_node is None:
            self.first_node = new_node
            self.last_node = self.first_node
        else:
            new_node.next = self.first_node
            self.first_node = new_node
            
    def remove_at_front(self):
        if self.is_empty():
            return 'Linked List is empty.'
        self.first_node = self.first_node.next
        
    
    def add_at_back(self, new_node):
        if self.is_empty():
            self.add_at_front()
        self.last_node.next = new_node
        self.last_node = new_node
    
    def remove_at_back(self):
        if self.is_empty():
            return 'Linked List is empty.'
        if self.first_node.next is None:
            self.first_node = None
            self.last_node = None
            return
        if self.first_node.next.next is None:
            self.last_node = self.first_node
            self.last_node.next = None
            return
        current_node = self.first_node
        while current_node.next.next is not None:
            current_node = current_node.next
        self.last_node = current_node
        self.last_node.next = None
    
    def __str__(self):
        if self.is_empty():
            return 'Linked List is empty.'
        node_values = []
        current_node = self.first_node
        while current_node is not None:
            node_values.append(current_node.data)
            current_node = current_node.next
        return str(node_values)
    
    def is_empty(self):
        return self.first_node is None
    
    
if __name__ == '__main__':
    new_node = Node(1)
    linked_list = LinkedList()
    linked_list.add_at_front(new_node)
    n2 = Node(2)
    linked_list.add_at_front(n2)
    n3 = Node(3)
    linked_list.add_at_front(n3)
    n4 = Node(4)
    linked_list.add_at_front(n4)
    n5 = Node(5)
    linked_list.add_at_front(n5)
    print(linked_list)
    linked_list.remove_at_front()
    print(linked_list)
    n6 = Node(-1)
    linked_list.add_at_back(n6)
    n7 = Node(-2)
    linked_list.add_at_back(n7)
    n8 = Node(-3)
    linked_list.add_at_back(n8)
    n9 = Node(-4)
    linked_list.add_at_back(n9)
    n10 = Node(-5)
    linked_list.add_at_back(n10)
    print(linked_list)
    linked_list.remove_at_back()
    print(linked_list)
    linked_list.remove_at_back()
    print(linked_list)
    linked_list.remove_at_back()
    print(linked_list)
    linked_list.remove_at_back()
    print(linked_list)
    linked_list.remove_at_back()
    print(linked_list)
    linked_list.remove_at_back()
    print(linked_list)
    linked_list.remove_at_back()
    print(linked_list)
    linked_list.remove_at_back()
    print(linked_list)
    linked_list.remove_at_back()
    print(linked_list)
    linked_list.remove_at_back()
    print(linked_list)