import random
from dataclasses import dataclass
from enum import Enum
import numpy as np
import itertools

@dataclass
class Person:
    name : str
    partner : str

# "Rasheed", "Aisha", "Yordi",
# "Kelly", "Cailin", "Landi", "Tina", "Sophia", "Anita", "Gaberial",
# "Estera", "Joshua", "Priti", "Samuel", "Chantelle", "Mirian", "Balveet"

men_arr = ["Rasheed", "Yordi","Cailin", "Landi", "Gaberial", "Joshua", "Samuel", "NULL"]
women_arry = ["Aisha", "Kelly", "Tina", "Sophia", "Anita", "Estera", "Priti", "Chantelle", "Mirian", "Balveet"]

possible_men_pairs = list(itertools.combinations(men_arr, 2))
possible_women_pairs = list(itertools.combinations(women_arry, 2))

def pretty_print(list):
    return [print(item) for item in list]

def check_pair_possible(pair, person_already_paired_map):
    for person in pair:
        if person_already_paired_map.get(person) is True:
            return False
    return True

def gen_all_uniqeue(pairs):
    person_connected_map = {}
    previous_pairs = {}
    all_possible_pairs = []
    possible_pairs = []
    while True:
        for pair in pairs:
            pair = list(pair)
            pair_string = ''.join(str(x) for x in pair)
            if previous_pairs.get(pair_string) == True:
                continue
            # iterate throuh each individual in the pair and check if they already have a partner
            if check_pair_possible(list(pair), person_connected_map):
                possible_pairs.append(pair)
                previous_pairs[pair_string   ] = True
                for person in pair:
                    person_connected_map[person] = True
        if possible_pairs == []:
            break
        all_possible_pairs.append(possible_pairs)
        person_connected_map = {}
        possible_pairs = []
        # break if no possible pairs
        # if they don't then add to pairs_list
    return all_possible_pairs

print(gen_all_uniqeue(possible_men_pairs))
print("----------------------------------")
# pretty_print(possible_women_pairs)




