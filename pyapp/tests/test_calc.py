import pytest
from pyapp.calc import calc


def test_addition():
    input_text = "1 + 0.5"
    expected = 1.5
    actual = calc(input_text)
    assert actual == expected


def test_subtraction():
    input_text = "1 - 3"
    expected = -2
    actual = calc(input_text)
    assert actual == expected

