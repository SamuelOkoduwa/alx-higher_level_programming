#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    
    total_weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)
    
    if total_weight == 0:
        return 0
    
    return total_weighted_sum / total_weight


# my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# result = weight_average(my_list)
# print("Average: {:0.2f}".format(result))
