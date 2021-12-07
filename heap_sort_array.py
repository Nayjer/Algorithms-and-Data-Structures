import math

array = ["x", 2, 1, 0, 22, 6]


def heapify_array(arr):
    height = int(math.log2(len(arr) - 1) // 1)
    for k in range(height):
        for level in range(height, k, -1):
            for i in range(2 ** level, 2 ** (level + 1), 2):
                if i + 1 > len(arr):
                    break
                elif i + 1 == len(arr):
                    if arr[i] > arr[i // 2]:
                        arr[i], arr[i // 2] = arr[i // 2], arr[i]
                else:
                    if arr[i] > arr[i + 1] and arr[i] > arr[i // 2]:
                        arr[i], arr[i // 2] = arr[i // 2], arr[i]
                    elif arr[i + 1] > arr[i] and arr[i + 1] > arr[i // 2]:
                        arr[i + 1], arr[i // 2] = arr[i // 2], arr[i + 1]
    return arr


sorted_array = []


def heap_sort(arr):
    if len(arr) == 1:
        return arr
    arr[1], arr[len(arr) - 1] = arr[len(arr) - 1], arr[1]
    sorted_array.append(arr[len(arr) - 1])
    arr.pop()
    i = 1
    while 2 * i < len(array) - 1:
        if arr[i] < arr[2 * i] and arr[2 * i] > arr[2 * i + 1]:
            arr[i], arr[2 * i] = arr[2 * i], arr[i]
            i = 2 * i
        elif arr[i] < arr[2 * i + 1] and arr[2 * i + 1] > arr[2 * i]:
            arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
            i = 2 * i + 1
        else:
            return heap_sort(arr)
    return heap_sort(arr)


arr1 = heapify_array(array)
print(arr1)
heap_sort(arr1)
print(sorted_array)
