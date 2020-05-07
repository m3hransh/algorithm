def max_sum_sub_brute_force(A):
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

