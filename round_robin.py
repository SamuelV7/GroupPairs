import numpy as np
import pandas as pd
from datetime import datetime, timedelta


men_arr = ["Rasheed", "Yordi", "Cailin", "Landi", "Gaberial", "Joshua", "Samuel"]
women_arry = ["Aisha", "Kelly", "Tina", "Sophia", "Anita", "Estera", "Priti", "Chantelle", "Mirian", "Balveet"]


make_even = lambda lst : lst if len(lst) % 2 == 0 else lst + ["Church"]

def week_range(date: datetime):
    return f"{date.date().strftime('%d/%m/%y')} -> {(date + timedelta(days=6)).date().strftime('%d/%m/%y')}"
    
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

def print_pairs_from_2d_arr(arr_2d, week):
    print("---------------------")
    print(f"{week}")
    print("---------------------")
    for i, item in enumerate(arr_2d[0]):
        print(f"{item} 🙏 {arr_2d[1][i]}")
    print("---------------------\n")

def deprecated_create_pairs(the_arr):
    rotated = np.array(the_arr)
    made_even = np.array(make_even(the_arr))
    rotated = made_even.reshape((2, len(make_even(the_arr)) // 2))
    print("")
    for i in range(len(make_even(the_arr))-1):
        print(f"Week {i+1}")
        rotated = rotate_partners(rotated.tolist())
        print_pairs_from_2d_arr(rotated, i)
        print("")

def create_pairs(the_arr):
    made_even = np.array(make_even(the_arr))
    the_arr = made_even.reshape(2, len(made_even) // 2)
    pairs_list = []
    for _ in range(len(made_even)-1):
        rotated = rotate_partners(the_arr.tolist())
        pairs_list.append(rotated)
        the_arr = rotated
    # [pretty_print(item, i+1) for i, item in enumerate(pairs_list)]
    return pairs_list

def create_weeks(pairs_list):
    [print_pairs_from_2d_arr(pairs, week_range(datetime.now() + timedelta(weeks=i))) for i, pairs in enumerate(pairs_list)]

create_weeks(create_pairs(men_arr))
create_weeks(create_pairs(women_arry))
