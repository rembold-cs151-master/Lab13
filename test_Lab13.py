"""
Basic tests for Lab07"
"""

import pytest
import os
from Lab13 import search_for_python


def test_returns_a_value():
    student = search_for_python('Search.txt')
    assert student is not None, "Did you remember to return something?"


def test_return_correct_value():
    student = search_for_python('Search.txt')
    assert student == 8, "There should be 8 python words in the search, but you are not finding all of them?"


def test_Foundtxt_created():
    student = search_for_python('Search.txt')
    assert os.path.exists('Found.txt'), "Found.txt is not being found. Are you creating it?"


def test_correct_entries_in_found():
    student = search_for_python('Search.txt')
    with open('Found.txt') as f:
        contents = f.read().splitlines()
    for pair in [[5,22],[6,50],[14,60],[37,89],[41,11],[55,9],[61,32],[80,69]]:
        is_found = False
        for line in contents:
            if str(pair[0]) in line and str(pair[1]) in line:
                is_found = True
        assert is_found, f"You should have had the location {pair} on some line, but it was not found."

