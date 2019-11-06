# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i = 0
    j = 0
    k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])
    return merge(left_half, right_half)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            i+= 1
        else:
            temp = arr[j]
            for k in range(j, i, -1):
                arr[k] = arr[k -1]
            arr[i] = temp
            i += 1
            j += 1
            mid += 1





def merge_sort_in_place(arr, l, r):
    if l >= r:
        return arr
    middle = (l + r) // 2
    merge_sort_in_place(arr, l, middle)
    merge_sort_in_place(arr, middle + 1, r)
    merge_in_place(arr, l, middle, r)
    return arr



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr


