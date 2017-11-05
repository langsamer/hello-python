#!python3.5

def calc(text):
    """evaluate an expression and return its result
    """
    return eval(text)


def run_tests():
    import sys
    print("Python {}".format(sys.version))
    input_text = "1 + 1/2"
    expected = 1.5
    actual = calc(input_text)
    assert actual == expected, "expected {}, got {}".format(expected, actual)

    
if __name__ == '__main__':
    run_tests()
