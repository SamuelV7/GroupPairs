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

men_arr = ["Rasheed", "Yordi","Cailin", "Landi", "Gaberial", "Joshua", "Samuel"]
women_arry = ["Aisha", "Kelly", "Tina", "Sophia", "Anita", "Estera", "Priti", "Chantelle", "Mirian", "Balveet"]

possible_men_pairs = list(itertools.combinations(men_arr, 2))
possible_women_pairs = list(itertools.combinations(women_arry, 2))

def pretty_print(list):
    return [print(item) for item in list]

pair_permutation_men = list(itertools.permutations(possible_men_pairs))
print(list(pair_permutation_men))
print("----------------------------------")
# pretty_print(possible_women_pairs)




