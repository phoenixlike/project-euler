import math

'''


'''

def sum_of_squares(num_list):
    return sum([math.pow(i, 2) for i in num_list])
     

def square_of_sum(num_list):
    return math.pow(sum(num_list), 2)


print square_of_sum(range(1, 101)) - sum_of_squares(range(1, 101))


