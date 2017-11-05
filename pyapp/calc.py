import pytest


def calc(text):
    """evaluate an expression and return its result
    """
    return eval(text)


if __name__ == '__main__':
    pytest.run()
