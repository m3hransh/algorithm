def maximum_subarray_rec(A, low, high):
    if low == high:
        return ((low,low), A[low])
    mid = (low + high) // 2
    left = maximum_subarray_rec(A, low, mid)
    right = maximum_subarray_rec(A, mid+1, high)
    cross = find_max_crossing_subarray(A, low, mid, high)

    return max( left, right, cross, key=lambda x: x[1])
