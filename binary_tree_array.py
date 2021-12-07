def insert_element(arr, element, i=1):  # array-implementation
    if i >= len(arr):
        arr += ["x" for i in range(len(arr), i + 1)]
        arr[i] = element
        return arr
    if arr[i] == "x":
        arr[i] = element
        return arr
    if element <= arr[i]:
        i = 2 * i
    elif element > arr[i]:
        i = 2 * i + 1
    return insert_element(arr, element, i)


def search_element(arr, element, i=1):
    while True:
        if arr[i] == element:
            print("Element " + str(element) + " found on index " + str(i))
            return
        elif arr[i] == "x" or i >= len(arr):
            print("Element " + str(element) + " not in the tree")
            return
        if element > arr[i]:
            i = 2 * i + 1
        elif element <= arr[i]:
            i = 2 * i


def count_elements(arr):
    count = str(sum([1 for i in arr if i != "x"]))
    levels = str(int(math.log2(len(arr))//1))
    print("In the tree are " + count + " elements with " + levels + " levels")
    
 
def delete_element(arr, i):
    height = int(math.log2(len(arr))//1)
    height_of_element = int(math.log2(i)//1)
    levels_to_redirect = height - height_of_element - 1
    if levels_to_redirect == 0:
        arr[i] = "x"
    else:
        c = 0
        while c < levels_to_redirect:
            if arr[i * 2] != "x":
                arr[i] = arr[i * 2]
                i = i * 2
            else:
                arr[i] = arr[i * 2 + 1]
                i = i * 2 + 1
            c += 1
        arr[i] = "x"


bin_tree = []
bin_tree = insert_element(bin_tree, 2)
bin_tree = insert_element(bin_tree, 5)
bin_tree = insert_element(bin_tree, 1)
bin_tree = insert_element(bin_tree, 2)
bin_tree = insert_element(bin_tree, 5)
bin_tree = insert_element(bin_tree, 1)
bin_tree = insert_element(bin_tree, 2)
bin_tree = insert_element(bin_tree, 5)
bin_tree = insert_element(bin_tree, 1)
print(bin_tree)
