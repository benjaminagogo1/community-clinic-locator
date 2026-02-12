"""Functions used in preparing Guido's gorgeous lasagna."""

# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time based on number of layers.

    :param number_of_layers: int - number of layers.
    :return: int - preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed time in minutes.

    :param number_of_layers: int - number of layers.
    :param elapsed_bake_time: int - time already baked.
    :return: int - total elapsed time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
