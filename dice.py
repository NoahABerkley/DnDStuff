""" die roller for dnd5e battle simulator """

import random
import datetime

random.seed(datetime.datetime.now())

def roll(count, die):
    """ roll the dice """
    return random.randint(count, die)
