import timeit

array = []
for i in range(100000000):
    array.append(i)


# STRETCH: implement Linear Search
def linear_search(arr = array, target = 50000000):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1  # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr = array, target = 50000000):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1
    not_found = True
    while not_found:
        half = (high + low) // 2
        if arr[half] == target:
            return half
        elif low == high:
            break
        elif arr[half] < target:
            low = half + 1
        elif arr[half] > target:
            high = half - 1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr = array, target = 50000000, low = 0,
                            high = len(array) - 1):
    middle = (low + high) // 2

    if len(arr) == 0:
        return -1  # array empty

    elif arr[middle] > target:
        return binary_search_recursive(arr, target, low,
                                       middle - 1)
    elif arr[middle] < target:
        return binary_search_recursive(arr, target, middle + 1,
                                       high)
    else:
        return middle


# elapsed_time = timeit.timeit(linear_search, number = 100) / 100
# print("linear search: ", elapsed_time)

elapsed_time = timeit.timeit(binary_search, number = 100) / 100
print("binary search: ", elapsed_time)

elapsed_time = timeit.timeit(binary_search_recursive, number = 100) / 100
print("binary search recursive: ", elapsed_time)
