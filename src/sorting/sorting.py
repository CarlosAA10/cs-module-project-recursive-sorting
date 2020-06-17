# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # start pointers at the start of both lists
    a, b = 0, 0
    #traverse both pointers through their respective lists
    for i in range(len(merged_arr)):
        # check if pointer is out of bounds of its respective aray
        # if it is, then we just need to copy every element from the other array
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b > len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # both indices are still in bounds of their respective arrays
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
        # compare the values at both pointers
        # whichever value is smaller, we copy that value to our merged list
        # increment that pointer


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # phase 1: keep splitting our arr until we ave lists of length 1
    if len(arr) > 1:
        left = merge_sort(arr[0:])


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

