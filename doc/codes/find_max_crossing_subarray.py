def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    temp = 0
    i = mid
    for k in range(mid, low-1, -1):
        temp += A[k]
        if temp > left_sum:
            left_sum = temp
            i = k
    right_sum = float('-inf')
    temp = 0
    j = mid + 1
    for k in range(mid+1, high+1):
        temp += A[k]
        if temp > right_sum:
            right_sum = temp
            j = k
    
    return ((i,j), left_sum + right_sum)
