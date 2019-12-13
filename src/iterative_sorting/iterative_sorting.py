# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        if i != smallest_index:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    for i in range(len(arr) -1):
        swapped = False
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j +1], arr[j]

        if not swapped:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum = -1):
    if len(arr) == 0:
        return arr
    for num in arr:
        if maximum < num:
            maximum = num

    count = [0] * (maximum + 1)
    for num in arr:
        count[num] = count[num] + 1
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"

    sorted_array = []
    for i, num in enumerate(count):
        while num > 0:
            sorted_array.append(i)
            num -= 1

    return sorted_array
