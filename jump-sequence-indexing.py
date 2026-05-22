"""
Please write a function named solve which accepts two arguments:
  -> jump_sequence: tuple[int, ...] is a sequence of non-negative integers
  -> start_index: int is the index at which you begin traversal of the tuple

Each element in jump_sequence represents the exact distance you can move, in either direction, from that index.
For example—from the start index, you can move to the index calculated by either of the following:
  -> start_index + jump_sequence[start_index]
  -> start_index - jump_sequence[start_index]
From each of the index(es) to which you are able to traverse, you may move in either direction the number of positions represented by the value at that index, repeat ad infinitum.

>> Your objective is to find an element in the tuple with the value 0,
   or determine that reaching an element having the value 0 is not possible.

>> The function should return a bool indicating True if you are able to reach 0,
   or False if it is not possible to reach a position in the tuple holding a 0 value.
Test Cases
"""
from fileinput import lineno

import numpy as np
import pandas as pd
from numpy.ma.core import count

# load tuple 1d arrays
sequence_list = [
    (1,(4, 9, 2, 100, 0), 2, True),
    (2,(1, 0, 9, 2, 100, 1), 3, True),
    (3,(0, 9), 1, False),
    (4,(1, 1, 0), 0, True),
    (5,(), 0, False),
    (6,(4, 9, 2, 100, 2), 2, False),
]


def solve():
    """find an element in the tuple with value 0, or determine not possible."""
    try:
        # indexer loop
        for row_sequence in sequence_list:

            # extract meta
            results_dict = {}
            row_number, nested_tuple, start_index, expected_result = row_sequence
            nested_tuple_length = len(nested_tuple)

            # handle edge cases
            if nested_tuple_length < 1:
                jump_value = None
                result_low = None
                result_high = None
                results = [result_low, result_high]

            elif nested_tuple_length < row_sequence[1][start_index]:
                jump_value = None
                result_low = None
                result_high = None
                results = [result_low, result_high]

            else:
                jump_value = row_sequence[1][start_index]
                result_low = nested_tuple[(start_index - jump_value)]
                result_high = nested_tuple[(start_index + jump_value)]
                results = [result_low, result_high]

            # classify outcomes
            if 0 in results:
                outcome = True
            else:
                outcome = False

            concordance = outcome == expected_result

            # display meta
            print(
                f'\nrow-level tuple: {row_sequence}'
                f'\n    row_number: {row_number}'
                f'\n    nested_tuple length: {nested_tuple_length}'
                f'\n    start_index: {start_index}'
                f'\n    jump_value: {jump_value}'
                f'\n    result_low: {result_low}'
                f'\n    result_high: {result_high}'
                f'\n    results [low, high]: {results}'
                f'\n    expected_result: {expected_result}'
                f'\n    outcome_result: {outcome}'
                f'\n    concordance: {concordance}'
            )

        return

    except Exception as e_solve:
        print('There was an ERROR: ', e_solve)

    finally:
        print('\n\nThe function solve() has completed.')


solve()

exit(0)









