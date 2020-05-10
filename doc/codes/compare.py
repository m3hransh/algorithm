import timeit
from random import randint
import matplotlib.pylab as plt

from maximum_subarray_sum import maximum_subarray_1, maximum_subarray_2, maximum_subarray_3


def func_timer(func, *args, **kwargs):
    '''Take a function and its arguments and return runtime.'''
    def wrap():
        func(*args, **kwargs)
    return timeit.timeit(wrap, number=10)


#Input samples
t = [10,100,500,1000,2000,3000,5000]

brute_force = []
recursive = []
greedy = []

for i in t:
    #creating random array
    A = [randint(-100, 100) for i in range(i)]
    d1 = func_timer(maximum_subarray_1, A)
    d2 = func_timer(maximum_subarray_2, A)
    d3 = func_timer(maximum_subarray_3, A)

    brute_force.append(d1)
    recursive.append(d2)
    greedy.append(d3)

#plotting the runtimes
plt.plot(t, brute_force,'r', label='Brute force')              
plt.plot(t, recursive,'g',label='Recursive')
plt.plot(t, greedy,'b',label='Greedy')
plt.legend()
plt.show()
