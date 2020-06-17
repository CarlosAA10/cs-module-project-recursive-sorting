# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, low,high):
    # Your code here
    # base cases 
    # we find our target at the midpoint or we deplete our range
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            #recurse
            return binary_search(arr, target, low, mid - 1)

        else: 
            return binary_search(arr, target, low , mid + 1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

