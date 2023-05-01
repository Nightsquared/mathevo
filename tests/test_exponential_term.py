import sys
sys.path.insert(0, '/Users/David/Documents/mathevo/terms')

from exponentialterm import ExponentialTerm

import pytest

exponential_evaluate_test_data = [
    #(a, b, x, expected, error), a * b^x
    (1, 2, 0, 1, 0.00001),
    (1, 2, 1, 2, 0.00001),
    (2, 3, 2, 18, 0.00001),
    (3, 0.5, 3, 0.375, 0.00001),
    (-1, 2, 2, -4, 0.00001),
]

@pytest.mark.parametrize("a, b, x, expected, error", exponential_evaluate_test_data)
def test_exponential_term_evaluate(a, b, x, expected, error):
    term = ExponentialTerm(a, b)
    result = term.evaluate(x)
    assert abs(result - expected) < error, f"Expected {expected}, but got {result}"


exponential_str_test_data = [
    #(a, b, expected_str)
    (1, 2, "2^x"),
    (2, 3, "2(3^x)"),
    (3, 0.5, "3(0.5^x)"),
    (-1, 2, "-2^x"),
    (0.5, 3, "0.5(3^x)"),
]

@pytest.mark.parametrize("a, b, expected_str", exponential_str_test_data)
def test_exponential_term_str(a, b, expected_str):
    term = ExponentialTerm(a, b)
    result = str(term)
    assert result == expected_str, f"Expected '{expected_str}', but got '{result}'"

def test_exponential_term_create_random():
    term1 = ExponentialTerm.create_random()
    term2 = ExponentialTerm.create_random()
    print(f"\nRandomly created exponential term 1: {term1}")
    print(f"Randomly created exponential term 2: {term2}")
    assert term1.a != term2.a or term1.b != term2.b, "Randomly created exponential terms had the same a and b values"

def test_exponential_term_mutate():
    term = ExponentialTerm(1, 2)
    print(f"\nExponential mutate test, before mutate: {term}")
    term.mutate()
    print(f"Exponential mutate test, after mutate: {term}")
    term.mutate()
    print(f"Exponential mutate test, after second mutate: {term}")
    term.mutate()
    print(f"Exponential mutate test, after third mutate: {term}")