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

def circular_list(person_list, index):
    if index == 0:
        return 0
    length = len(person_list)
    return person_list[(index) % length]

# circular_list(men_arr, men_arr[2])

# output = circular_list(men_arr, 2)+ 9

def gen_all_possible(the_list):
    jumps = 1
    person_claimed = {}
    while jumps != len(the_list):
        for i, person in enumerate(the_list):
            if person_claimed.get(person) != True:
                person_claimed[person] = True
                jumped_location = i + jumps
                persons_pair = circular_list(the_list, jumped_location)
                if person_claimed.get(persons_pair) != True:
                    person_claimed[persons_pair] = True
                    print(f"{person} with {persons_pair} WEEK {jumps}")
        print("----------------------------------")
        person_claimed = {}
        jumps += 1


# gen_all_possible(men_arr)
print("----------------------------------")
# print(pretty_print(gen_all_uniqeue(possible_women_pairs)))


# define the list of players
players = ['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8']


import random

# define the list of players
players = men_arr


# shuffle the list of players
random.shuffle(players)

# shuffle the list of players
results = []

# loop through the rounds
for round in range(len(players) - 1):
  # create a list of matches for this round
  round_matches = []
  # if this is the first round, pair the top half with the bottom half
  if round == 0:
    # loop through the players in the top half of the list
    for i in range(len(players) // 2):
      # pair the top player with the bottom player
      round_matches.append((players[i], players[len(players) - i - 1]))
  # if this is the second round or later, pair the players within the top half
  else:
    # loop through the players in the top half of the list
    for i in range(len(players) // 2):
      # pair the current player with the next player
      round_matches.append((players[i], players[i + 1]))
  # add a bye for the remaining player
  round_matches.append((players[len(players) // 2], None))
  # add the matches to the results list
  results.append(round_matches)
  # rotate the list of players
  players.insert(1, players.pop())

# print the results
print(results)


# results = create_tournament(men_arr)

# results_women = create_tournament(women_arry)
# print the results




