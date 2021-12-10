import math

array = ["x", 110, 514, -239, -428, -342, 644, -762, -985, 85, 619, -712, 985, 579, -57, 254, 151, 500, 692, 171, 874, -312, 222, 159, 880, 90, 916, 613, 747, 539, 420]


def heapify_array(arr):
    height = int(math.log2(len(arr) - 1) // 1)
    for k in range(height):  # (log n)^2 * n comparisons
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


def heap_sort(arr, sorted_array):
    if len(arr) == 1:
        return sorted_array
    arr[1], arr[len(arr) - 1] = arr[len(arr) - 1], arr[1]
    sorted_array.append(arr[len(arr) - 1])
    arr.pop()
    i = 1
    if len(arr) == 3:
        if arr[i] < arr[2 * i]:
            arr[i], arr[2 * i] = arr[2 * i], arr[i]
        else:
            return heap_sort(arr, sorted_array)
    else:
        while 2 * i < len(array) - 1:  # log n * n comparisons
            if arr[i] < arr[2 * i] and arr[2 * i] > arr[2 * i + 1]:
                arr[i], arr[2 * i] = arr[2 * i], arr[i]
                i = 2 * i
            elif arr[i] < arr[2 * i + 1] and arr[2 * i + 1] > arr[2 * i]:
                arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
                i = 2 * i + 1
            else:
                return heap_sort(arr, sorted_array)
    return heap_sort(arr, sorted_array)


arr1 = heapify_array(array)
print(heap_sort(arr1, []))
