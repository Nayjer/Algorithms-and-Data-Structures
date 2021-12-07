import random
import time


def linear_search(array, element):
    for i in range(len(array)):
        if element == array[i]:
            return i


def binary_search(array, element):
    start = 0
    end = len(array)
    while start <= end:
        mid = (start + end) // 2
        if element == array[mid]:
            return mid
        elif element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def binary_search_index(array, element):
    start = 0
    end = len(array)
    while start <= end:
        mid = (start + end) // 2
        if element == array[mid]:
            return mid
        elif element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end


def find_max(array):
    save = 0
    for i in range(1, len(array)):
        if array[i] > array[save]:  # worst- and best-case = len(array)-1
            save = i
    return save


def find_min(array):
    save = 0
    for i in range(1, len(array)):
        if array[i] < array[save]:  # equals find_max
            save = i
    return save


def selection_sort(array):
    for i in range(len(array)-1):
        q = find_min(array[i:len(array)]) + i  # 1 + 2 + ... len(array)-1 = 0,5*len(array)²-0,5*len(array) operations
        z = array[i]
        array[i] = array[q]  # 3 * (len(array) -1) movements
        array[q] = z
    return array


def insertion_sort(array):
    for i in range(1, len(array)):  # saving each element except first = len(array)-1 movements
        for j in range(i-1, -1, -1):  # in worst-case: 1 + 2 + ... + len(array)-1 op. = 0,5*len(array)²-0,5*len(array)
            if array[j+1] < array[j]:  # in worst-case: 3 * (len(array) -1) movements
                z = array[j+1]
                array[j+1] = array[j]
                array[j] = z
    return array


def insertion_sort_optimized(array):
    for i in range(1, len(array)):
        k = 0
        index = array[i]
        for j in range(i-1, -1, -1):
            if index < array[j]:
                array[j+1] = array[j]
                k += 1
        array[i-k] = index
    return array


def insertion_sort_binary_optimized(array):
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            index = binary_search_index(array[0:i], array[i])
            if array[index] < array[i]:
                for j in range(i - 1, index-1, -1):
                    array[j + 1] = array[j]
            array[index] = array[i]
    return array


def bubble_sort(array):
    iterations = 0
    while 1:
        count = 0
        for i in range(len(array)-(iterations+1)):  # after each iteration the last element is the maximum
            if array[i] > array[i+1]:  # in worst-case: 0,5*(len(array)-(iterations+1))²-0,5*(len(array)-(iterations+1)) operations per iteration
                count += 1  # in worst-case we would need len(array)-1 iterations
                z = array[i]
                array[i] = array[i+1]
                array[i+1] = z
        iterations += 1
        if count == 0:
            break
    return array


def counting_sort(array):
    array_two = []  # the list where we put in our elements
    for i in range(array[find_max(array)]+1):  # we need minimum a length of our highest element
        array_two.append(0)
    for i in array:
        array_two[i] += 1  # for each element of the unsorted array, add 1 to the index according to array_two
    sorted_array = []
    for i in range(1, len(array_two)):  # if the element of each index is higher then 0 append each 1 to the final_array
        if array_two[i] > 0:
            while array_two[i] != 0:
                sorted_array.append(i)
                array_two[i] -= 1
    return sorted_array


def radix_sort(array):
    count = len(str(array[find_max(array)]))  # how much I need to iterate depends on the number of digits from the max
    for c in range(1, count+1):
        coefficient_list = []
        for i in range(10):  # list with lists, each represents a possible digit (0 - 9)
            coefficient_list.append([])
        for element in array:
            try:
                coefficient_list[int(str(element)[-c])].append(element)  # gets the c-last digit of each element and append it to the belonging coefficient list
            except IndexError:
                coefficient_list[0].append(element)  # when theres no c-last digit append the element to the first coefficient list
        array.clear()
        for i in coefficient_list:
            for j in i:
                array.append(j)
    return array


def merge_sort_recursive(array):
    middle = len(array) // 2
    left = array[:middle]  # --> not in-place
    right = array[middle:]  # list gets split into two lists with equal length
    if len(array) > 1:
        #  print("Array: " + str(array))
        #  print("Left: " + str(left) + "  Right: " + str(right))
        #  print("----------")
        merge_sort_recursive(left)
        merge_sort_recursive(right)
        i = 0  # left-side index
        j = 0  # right-side index
        z = 0  # index to edit the array
        while i < len(left) and j < len(right):  # left and right side gets merged
            if left[i] <= right[j]:  # each comparison (len(array) - 1 in total) creates one ordered element in the
                # array -> (n-1)*log(n) comparisons in total for the array
                array[z] = left[i]  # we always choose the left key -> is stable
                i += 1
            else:
                array[z] = right[j]
                j += 1
            z += 1
        while i < len(left):  # when there are any elements untouched in the left or right side
            array[z] = left[i]
            z += 1
            i += 1
        while j < len(right):
            array[z] = right[j]
            z += 1
            j += 1
        #  print(left, "+ " + str(right), "---> " + str(array))
        return array

    
def merge_sort_iterative(array):
    n = len(array)
    k = 1
    while k < n:
        for f in range(0, n//k, 2):
            left, right = array[f*k: (f+1)*k], array[(f+1)*k: (f+2)*k]
            i = 0  # left-side index
            j = 0  # right-side index
            z = f*k  # index to edit the array
            while i < len(left) and j < len(right):  # left and right side gets merged
                if left[i] <= right[j]:  # each comparison (len(array) - 1 in total) creates one ordered element in the
                    # array -> (n-1)*log(n) comparisons in total for the array
                    array[z] = left[i]  # we always choose the left key -> is stable
                    i += 1
                else:
                    array[z] = right[j]
                    j += 1
                z += 1
            while i < len(left):  # when there are any elements untouched in the left or right side
                array[z] = left[i]
                z += 1
                i += 1
            while j < len(right):
                array[z] = right[j]
                z += 1
                j += 1
            #  print(left, "+ " + str(right), "---> " + str(array))
        k *= 2
    return array    
    

def main():
    print("*-----------------------------------------------------------------------------------*")
    print('''1: bubble-sort, 2: selection-sort, 3: insertion-sort, 4: counting-sort, 5: radix-sort''')
    print("*-----------------------------------------------------------------------------------*")
    print('''            6: binary-search, 7: linear-search, 8: binary-search-recursive           ''')
    print("*-----------------------------------------------------------------------------------*")
    print('''            9: merge-sort-recursive, 10: merge-sort-iterative                        ''')
    print("*-----------------------------------------------------------------------------------*")
    name = input(": ")
    if name == "1":
        start = time.time()
        result = bubble_sort(arr)
        end = time.time()
        print("Bubble-Sort time needs: " + str(end - start))
        print(result)
        print("*-----------------------------------------------------------------------------------*")
    if name == "2":
        start = time.time()
        result = selection_sort(arr)
        end = time.time()
        print("Selection-Sort time needs: " + str(end - start))
        print(result)
        print(" ")
    if name == "3":
        start = time.time()
        result = insertion_sort_binary_optimized(arr)
        end = time.time()
        print("Insertion-Sort time needs: " + str(end - start))
        print(result)
        print(" ")
    if name == "4":
        start = time.time()
        result = counting_sort(arr)
        end = time.time()
        print("Counting-Sort time needs: " + str(end - start))
        print(result)
        print(" ")
    if name == "5":
        start = time.time()
        result = radix_sort(arr)
        end = time.time()
        print("Radix-Sort time needs: " + str(end - start))
        print(result)
        print(" ")
    if name == "6":
        start = time.time()
        result = binary_search(arr, 220)
        end = time.time()
        print("Binary-Search time needs: " + str(end - start))
        print(result)
        print("*-----------------------------------------------------------------------------------*")
    if name == "7":
        start = time.time()
        result = linear_search(arr, 220)
        end = time.time()
        print("Linear-Search time needs: " + str(end - start))
        print(result)
        print("*----------------------------------------------------------------------------------*")
    if name == "8":
        start = time.time()
        binary_search_recursive(arr, 220, 0, len(arr))
        end = time.time()
        print("Binary-Search-Recursive time needs: " + str(end - start))
        print("*-----------------------------------------------------------------------------------*")
    if name == "9":
        start = time.time()
        result = merge_sort_recursive(arr)
        end = time.time()
        print("Merge-Sort-Recursive time needs: " + str(end - start))
        print(result)
        print("*-----------------------------------------------------------------------------------*")
    if name == "10":
        start = time.time()
        result = merge_sort_iterative(arr)
        end = time.time()
        print("Merge-Sort-Iterative time needs: " + str(end - start))
        print(result)
        print("*-----------------------------------------------------------------------------------*")


arr = []
for o in range(30):
    arr.append(random.randint(1, 999))
print("array: " + str(arr))

while True:
    main()
