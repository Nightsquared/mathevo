import sys 
sys.path.insert(0, '/Users/David/Documents/mathevo/terms')

from polynomialterm import PolynomialTerm

import pytest

polynomial_evaluate_test_data = [
    #(a, b, x, expected, error = .00001), ax ^ b
    (1, 1, 3, 3, 0.00001),
    (1, 2, 3, 9, 0.00001),
    (9, 0, 3, 9, 0.00001),
    (9, 2, -3, 81, 0.00001),
    (9, 3, -3, -243, 0.00001),
    (1, -2, 3, 1/9, .00001),
]

@pytest.mark.parametrize("a, b, x, expected, error", polynomial_evaluate_test_data)
def test_polynomial_term_evaluate(a, b, x, expected, error):
    term = PolynomialTerm(a, b)
    result = term.evaluate(x)
    assert abs(result - expected) < error, f"Expected {expected}, but got {result}"



polynomial_integrate_test_data = [
    #(a, b, lower, upper, expected, steps = 40, error = .1), ax ^ b
    (1, 2, 0, 2, 8/3, 40, .1),
    (1, 2, -2, 2, 16/3, 40, .1),
    (1, 3, -2, 2, 0, 40, .1),
    (1, 3, -4, 2, -60, 40, .1),
    (0, 3, -4, 2, 0, 40, .1),
    (1/12, 4, -2, 2, 16/15, 40, .1),
    (12, 4, -2, 2, 768/5, 100, .1),
]

@pytest.mark.parametrize("a, b, lower, upper, expected, steps, error", polynomial_integrate_test_data)
def test_polynomial_term_integrate(a, b, lower, upper, expected, steps, error):
    term = PolynomialTerm(a, b)
    result = term.integrate(lower, upper, steps)
    assert abs(result - expected) < error, f"Expected {expected}, but got {result}"



polynomial_str_test_data = [
    #(a, b, expected_str)
    (1, 2, "x^2"),
    (-1, 2, "-x^2"),
    (3, 1, "3x"),
    (5, 3, "5x^3"),
    (-4, 2, "-4x^2"),
    (0, 3, "0x^3"),
    (2.5, 1, "2.5x"),
    (-0.5, 2, "-0.5x^2"),
    (1, -2, "x^-2"),
    (-1, -3, "-x^-3"),
    (73678289, -188432, "73678289x^-188432"),
]

@pytest.mark.parametrize("a, b, expected_str", polynomial_str_test_data)
def test_polynomial_term_str(a, b, expected_str):
    term = PolynomialTerm(a, b)
    result = str(term)
    assert result == expected_str, f"Expected '{expected_str}', but got '{result}'"

def test_polynomial_term_create_random():
    term1 = PolynomialTerm.create_random()
    term2 = PolynomialTerm.create_random()
    print(f"\nRandomly created polynomial term 1: {term1}")
    print(f"Randomly created polynomial term 2: {term2}")
    assert term1.a != term2.a, f"Randomly created polynomial terms had the same a value, {term1.a}'"

def test_polynomial_term_mutate():
    term = PolynomialTerm()
    print(f"\nPolynomial mutate test, before mutate: {term}")
    term.mutate()
    print(f"\nPolynomial mutate test, after mutate: {term}")
    term.mutate()
    print(f"\nPolynomial mutate test, after second mutate: {term}")
    term.mutate()
    print(f"\nPolynomial mutate test, after third mutate: {term}")
