import sys 
sys.path.insert(0, '/Users/David/Documents/mathevo/terms')

from polynomialterm import PolynomialTerm

import pytest

polynomialintegraltestdata = [
    #(a, b, lower, upper, expected, steps = 40, error = .1), ax ^ b
    (1, 2, 0, 2, 8/3, 40, .1),
    (1, 2, -2, 2, 16/3, 40, .1),
    (1, 3, -2, 2, 0, 40, .1),
    (1, 3, -4, 2, -60, 40, .1),
    (0, 3, -4, 2, 0, 40, .1),
    (1/12, 4, -2, 2, 16/15, 40, .1),
    (12, 4, -2, 2, 768/5, 100, .1),
]

@pytest.mark.parametrize("a, b, lower, upper, expected, steps, error", polynomialintegraltestdata)
def test_polynomial_term_integrate(a, b, lower, upper, expected, steps, error):
    term = PolynomialTerm(a, b)
    result = term.integrate(lower, upper, steps)
    assert abs(result - expected) < error, f"Expected {expected}, but got {result}"