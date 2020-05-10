def maximum_subarray_3(A):
    # S_i is the maximum subarray the end in index i
    maximum = float('-inf')
    index = (-1, -1)
    si = 0
    start = 0
    for i in range(len(A)):
        if si <=0:
            si = A[i] 
            start = i
        else:
            si += A[i]
        if si > maximum:
            maximum = si
            index = (start, i) 

    return (index, maximum)
