import random
import numpy as np
import pandas as pd

men_arr = ["Rasheed", "Yordi", "Cailin", "Landi", "Gaberial", "Joshua", "Samuel"]
women_arry = ["Aisha", "Kelly", "Tina", "Sophia", "Anita", "Estera", "Priti", "Chantelle", "Mirian", "Balveet"]


make_even = lambda lst : lst if len(lst) % 2 == 0 else lst + ["Church"]
rotate_left = lambda lst, by : [lst[(i + by) % len(lst)] for i, _ in enumerate(lst)]
full_circle = lambda lst : [rotate_left(lst, i) for i, _ in enumerate(lst)]

# make a 2d array


# print(men_np.tolist())

def rotate_partners(np_arr_2d):
    # take the first element of the second array inside given array
    # take first array and remove 1 - since 1 on the left handside will always be there

    arr_1_head = np_arr_2d[0][0]
    # removing the last item in the first array
    arr_1_tail_removed = np_arr_2d[0][1: -1]

    # now add the first item from second array to the beginner of arr 1
    # add last item from first array into the end of second array
    arr_2 = np_arr_2d[1]
    arr_2_head_removed = np_arr_2d[1][1:]
    arr_2_first_item = np_arr_2d[1][0]

    first_array = [arr_1_head] + [arr_2_first_item] + arr_1_tail_removed 
    second_array = arr_2_head_removed + [np_arr_2d[0][-1]]
    
    return np.array([first_array, second_array])

def pretty_print(arr_2d):
    for i, item in enumerate(arr_2d[0]):
        print(f"{item} partnered with {arr_2d[1][i]}")

def create_pairs(the_arr):
    rotated = np.array(the_arr)
    made_even = np.array(make_even(the_arr))
    rotated = made_even.reshape((2, len(make_even(the_arr)) // 2))
    print("")
    for i in range(len(make_even(the_arr))-1):
        rotated = rotate_partners(rotated.tolist())
        pretty_print(rotated)
        print("")


create_pairs(men_arr)
create_pairs(women_arry)