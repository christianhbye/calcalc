from argparse import ArgumentParser
import numpy as np
import pytest

parser = ArgumentParser(description="")
parser.add_argument(
    "Expression",
    type=str,
    help="Input string to calculator. Either to be evaluated by the "
    "calculator (default) or to be requested to WolframAlpha.",
)
parser.add_argument(
    "-w",
    type=bool,
    default=False,
    help="Send input to WolframAlpha or not. Default is false",
)
args = parser.parse_args()


def calculate(expression):
    return eval(expression)


def test_not_string():
    """
    Calculate should not work when something else than a string is input
    """
    with pytest.raises(TypeError):
        calculate(15)  # int
    with pytest.raises(TypeError):
        calculate([1.0, 2.3, 3.4])  # list of floats
    with pytest.raises(TypeError):
        calculate(None)  # none
    with pytest.raises(TypeError):
        calculate(False)  # bool


def test_unexpected_string():
    """
    Calculate should not work when a string has a non-math character
    """
    with pytest.raises(NameError):  # h should be intepreted as undefined
        calculate("2+h")


def test_add_subtract():
    """
    Test adding and subtracting two ints with calculate.
    """
    TOL = 1e-4  # tolerance
    x1, x2 = 12, 15  # numbers to add
    s = x1 + x2  # sum as computed by python (the true value)
    str_sum = f"{x1}+{x2}"  # expression to input to calculate
    assert np.isclose(s, calculate(str_sum), atol=TOL)
    diff = x1 - x2
    str_diff = f"{x1}-{x2}"
    assert np.isclose(diff, calculate(str_diff), atol=TOL)


def test_add_many():
    """
    Add many random floats (positve or negative)
    """
    TOL = 1e-4
    N_NUMS = 10  # number of floats to add
    LOW, HIGH = -100, 100
    floats = np.random.uniform(low=LOW, high=HIGH, size=N_NUMS)
    true_sum = floats.sum()  # sum as computed by numpy
    str_sum = "+".join([str(f) for f in floats])  # remove last +
    assert np.isclose(true_sum, calculate(str_sum), atol=TOL)


def test_multiply_div():
    """
    Test multiplying and dividing numbers
    """
    TOL = 1e-4  # tolerance
    x1, x2 = 12, 15  # numbers to multiply/divide
    prod = x1 * x2  # product as computed by python (the true value)
    str_prod = f"{x1}*{x2}"  # expression to input to calculate
    assert np.isclose(prod, calculate(str_prod), atol=TOL)
    div = x1 / x2
    str_div = f"{x1}/{x2}"
    assert np.isclose(div, calculate(str_div), atol=TOL)


def test_div0():
    """
    Test that dividing by 0 throws and error
    """
    with pytest.raises(ZeroDivisionError):
        calculate("1/0")


def test_power():
    """
    Test computing powers
    """
    TOL = 1e-4  # tolerance
    x1, x2 = 2, 4  # numbers to multiply/divide
    power = x1**x2  # product as computed by python (the true value)
    str_power = f"{x1}**{x2}"  # expression to input to calculate
    assert np.isclose(power, calculate(str_power), atol=TOL)


def test_order():
    """
    Test inputting () to define order of operations
    """
    TOL = 1e-4  # tolerance
    x1, x2, x3 = 4, 3, 5
    true = (x1 + x2) * x3  # () is respected
    false = x1 + x2 * x3  # () is ignored
    str_exp = f"({x1}+{x2})*{x3}"
    assert np.isclose(true, calculate(str_exp), atol=TOL)
    assert not np.isclose(false, calculate(str_exp), atol=TOL)


def test_combination():
    """
    Test some long expression involving multiple operations (integration test)
    """
    TOL = 1e-4  # tolerance
    x1, x2, x3, x4, x5, x6 = 1, 1.2, 0.9, 37, 14, 2
    exp = x1 / x2**x3 + (x4 - x5) * x6
    str_exp = f"{x1}/{x2}**{x3}+({x4}-{x5})*{x6}"
    assert np.isclose(exp, calculate(str_exp), atol=TOL)


if __name__ == "__main__":
    ans = calculate(args.Expression)
    print(ans)
