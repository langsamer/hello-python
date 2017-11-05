import pytest
from pyapp.api import CalcApi


@pytest.fixture(scope='module')
def calc():
    ca = CalcApi()
    return ca.calc

def test_addition(calc):
    input_text = "1 + 0.5"
    expected = 1.5
    actual = calc(input_text)
    assert actual == expected


def test_subtraction(calc):
    input_text = "1 - 3"
    expected = -2
    actual = calc(input_text)
    assert actual == expected

