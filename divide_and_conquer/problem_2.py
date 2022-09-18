def binarysearch(arr, l, r, x):
    """Binary search algorithm  
    Args:
        arr: array
        l: left index
        r: right index
        x: element to search

    Returns: 
        index of element x in array arr

    """
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr, l, mid - 1, x)
        else:
            return binarysearch(arr, mid + 1, r, x)
    else:
        return -1
        