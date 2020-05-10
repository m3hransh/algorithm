#section:brute_force
def maximum_subarray_1(A):
    '''Return a tuple(range i,j,sum).

    argument:
    A -- list of numbers.
    '''
    max_sum =float('-inf')
    index = (-1,-1)
    for i in range(len(A)):
        temp =0
        for j in range(i, len(A)):
            temp += A[j]
            if temp > max_sum:
                max_sum = temp
                index =(i, j)
    
    return (index, max_sum)

#endsection


#section:find_max_crossing_subarray
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
#endsection


#section:devide_and_conquer
def maximum_subarray_rec(A, low, high):
    if low == high:
        return ((low,low), A[low])
    mid = (low + high) // 2
    left = maximum_subarray_rec(A, low, mid)
    right = maximum_subarray_rec(A, mid+1, high)
    cross = find_max_crossing_subarray(A, low, mid, high)

    return max( left, right, cross, key=lambda x: x[1])
#endsection
def maximum_subarray_2(A):
    return maximum_subarray_rec(A, 0, len(A)-1)
#section:greedy
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
#endsection


if __name__ == "__main__":
    A = list(map(int, input('Enter your array:\n').split()))
    (i,j), s = maximum_subarray_3(A)
    print('''your maximum subarray is:{}
            The sum is:{} '''.format(A[i:j+1], s))
