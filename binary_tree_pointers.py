class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinaryTree:
    
    """
    Binary trees are used to store data efficiently, for example in databases.
    Time-complexity is determined by the height of the tree: log_2(number_of_elements) // 1 <= height <= number_of_elements - 1
    In average we have 1,33*log(n) comparisons.
    """
    
    def __init__(self):
        self.start_node = None

    def search_element(self, value):
        n = self.start_node
        i = 0
        while True:
            if n is None:
                print("Element " + str(value) + " is not the in tree")
                break
            if n.value == value:
                print("Element " + str(value) + " got found in level " + str(i))
                break
            else:
                if value < n.value:
                    n = n.left_child
                elif value > n.value:
                    n = n.right_child
                i += 1

    def insert_element(self, value):
        new_node = Node(value)
        n = self.start_node
        if n is None:
            self.start_node = new_node
            print("Element " + str(value) + " is now the start_node")
        else:
            i = 1
            while True:
                if n.left_child is None and value <= n.value:
                    n.left_child = new_node
                    new_node.parent = n
                    print("Element " + str(value) + " got inserted on the left after element " + str(
                        n.value) + " at level " + str(i))
                    break
                elif n.right_child is None and value > n.value:
                    n.right_child = new_node
                    new_node.parent = n
                    print("Element " + str(value) + " got inserted on the right after element " + str(
                        n.value) + " at level " + str(i))
                    break
                else:
                    if value <= n.value:
                        n = n.left_child
                    elif value > n.value:
                        n = n.right_child
                    i += 1

    def traverse_pre_order(self, n, arr):
        if n is None:
            return arr
        else:
            arr.append(n.value)
            if n.left_child is not None:
                self.traverse_pre_order(n.left_child, arr)
            if n.right_child is not None:
                self.traverse_pre_order(n.right_child, arr)
            return arr

    def traverse_in_order(self, n, arr):
        if n is None:
            return arr
        else:
            if n.left_child is not None:
                self.traverse_in_order(n.left_child, arr)
            arr.append(n.value)
            if n.right_child is not None:
                self.traverse_in_order(n.right_child, arr)
            return arr

    def traverse_post_order(self, n, arr):
        if n is None:
            return arr
        else:
            if n.left_child is not None:
                self.traverse_post_order(n.left_child, arr)
            if n.right_child is not None:
                self.traverse_post_order(n.right_child, arr)
            arr.append(n.value)
            return arr


new_binary_tree = BinaryTree()
new_binary_tree.search_element(2)
new_binary_tree.insert_element(3)
new_binary_tree.insert_element(4)
new_binary_tree.insert_element(5)
new_binary_tree.insert_element(6)
new_binary_tree.search_element(1)
new_binary_tree.insert_element(1)
new_binary_tree.insert_element(0)
new_binary_tree.insert_element(-2)
new_binary_tree.insert_element(2)
new_binary_tree.insert_element(1)
new_binary_tree.insert_element(6)
new_binary_tree.insert_element(7)
array = []
new_binary_tree.traverse(new_binary_tree.start_node, array)
print(array)
