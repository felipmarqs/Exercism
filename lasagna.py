
"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time:int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    elapsed_bake_time = elapsed_bake_time
    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time_remaining

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(layers:int):
    """Calculate the preparation time in minutes

    :param layers: int - ammount of layers for the lasagna
    :return: int - minutes the lasagna needs to be prepared 

    Function that takes the actual amount of layers as an argument and returns how many
    minutes it needs to be prepared based on the 'PREPARATION_TIME'.
     """
    preparation_time_in_minutes = PREPARATION_TIME * layers
    return preparation_time_in_minutes

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers:int, elapsed_bake_time:int):
    """Calculate the elapsed time in minutes to prepare the entire lasagna

    :param number_of_layers: int - amount of layers
    :param elapsed_bake_time: int - minutes elapsed since the start of the preparation
    
    Function that takes the number of layers and the elapsed bake time and returns how many minutes
    it needs to prepare and bake the lasagna
    
    
    """
    elapsed_time_in_minutes = (number_of_layers * PREPARATION_TIME) + elapsed_bake_time
    return elapsed_time_in_minutes