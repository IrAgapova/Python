my_list = [i for i in range (99,1001) if i % 2 == 0]
from functools import reduce
def my_sum (prev_el, el):
    return prev_el * el
print (reduce (my_sum, my_list) )


