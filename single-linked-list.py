class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def count_list(self):
        if self.start_node is None:
            return 0
        else:
            n = self.start_node
            c = 0
            while n is not None:
                c += 1
                n = n.ref
            return c

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node  # link to the now second element
        self.start_node = new_node  # then declare that the new element is the start node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:  # if theres no element in the list
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node  # if n.ref is None, we need to link this Node to our new Node

    def insert_at_index(self, index, data):
        if index == 0:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 0
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i += 1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_at_index(self, index):
        if index == 0:
            self.start_node = self.start_node.ref
            return
        i = 0
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i += 1
        if n is None:
            print("Index out of bound")
        else:
            n.ref = n.ref.ref

    def reverse_list(self, count):
        x = self.start_node
        i = 0
        n = self.start_node
        k = None
        while i < count - 1 and n is not None:
            k = n
            n = n.ref
            i += 1
        if n is None:
            print("Index out of bound")
        else:
            n.ref.ref = k.ref
            self.start_node = n.ref
        for c in range(count - 1, 1, -1):
            i = 0
            n = x
            k = None
            while i < c - 1 and n is not None:
                k = n
                n = n.ref
                i += 1
            if n is None:
                print("Index out of bound")
            else:
                n.ref.ref = k.ref
        x.ref.ref = x
        x.ref = None


new_linked_list = LinkedList()
new_linked_list.insert_at_end(1)
new_linked_list.insert_at_end(2)
new_linked_list.insert_at_end(4)
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_start(-22)
new_linked_list.insert_at_end(8)
new_linked_list.insert_at_index(3, 9)
new_linked_list.traverse_list()
print("--------------")
new_linked_list.reverse_list(new_linked_list.count_list()-1)
new_linked_list.traverse_list()
print(new_linked_list.count_list())
