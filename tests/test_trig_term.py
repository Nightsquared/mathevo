import sys
sys.path.insert(0, '/Users/David/Documents/mathevo/terms')

from trigterm import TrigTerm
import pytest
import math

trig_evaluate_test_data = [
    #(a, b, c, trig_function, x, expected, error), atrig_function(bx+c)
    (1, 1, 0, "sin", 0, 0, 0.00001),
    (1, 1, 0, "cos", 0, 1, 0.00001),
    (-4, 1, 0, "cos", 0, -4, 0.00001),
    (1, 1, math.pi/2, "sin", 0, 1, 0.00001),
    (2, 2, 0, "cos", math.pi/4, 0, 0.00001),
    (3, 1, -math.pi, "tan", math.pi/4, 3, 0.00001),
]

@pytest.mark.parametrize("a, b, c, trig_function, x, expected, error", trig_evaluate_test_data)
def test_trig_term_evaluate(a, b, c, trig_function, x, expected, error):
    term = TrigTerm(a, b, c, trig_function)
    result = term.evaluate(x)
    assert abs(result - expected) < error, f"Expected {expected}, but got {result}"


trig_integrate_test_data = [
    #(a, b, c, trig_function, lower, upper, expected, steps, error)
    (1, 1, 0, "sin", -2, 2, 0, 40, 0.1),
    (1, 1, 0, "sin", 0, math.pi, 2, 40, 0.1),
    (5, 1/2, math.pi, "sin", 0, math.pi, -10, 40, 0.1),
    (-3, 3, -5, "cos", -4, 1, 1.87, 40, 0.1),
    (1/3, 1/4, 0, "tan", 0, 1.99*math.pi, 6.46, 40, 1),
    (1/3, 1/4, 0, "tan", 0, 1.99*math.pi, 6.46, 400, .1),
]

@pytest.mark.parametrize("a, b, c, trig_function, lower, upper, expected, steps, error", trig_integrate_test_data)
def test_trig_term_integrate(a, b, c, trig_function, lower, upper, expected, steps, error):
    term = TrigTerm(a, b, c, trig_function)
    result = term.integrate(lower, upper, steps)
    assert abs(result - expected) < error, f"Expected {expected}, but got {result}"



trig_str_test_data = [
    #(a, b, c, trig_function, expected_str)
    (1, 1, 0, "sin", "sin(x)"),
    (2, 2, math.pi, "cos", "2cos(2x + 180°)"),
    (3, 0.5, -math.pi/4, "tan", "3tan(0.5x - 45°)"),
    (-1, -1, 0, "sin", "-sin(-x)"),
    (1.5, 1, -math.pi, "cos", "1.5cos(x - 180°)"),
    (1, -5, -math.pi/6, "sin", "sin(-5x - 30°)"),
]

@pytest.mark.parametrize("a, b, c, trig_function, expected_str", trig_str_test_data)
def test_trig_term_str(a, b, c, trig_function, expected_str):
    term = TrigTerm(a, b, c, trig_function)
    result = str(term)
    assert result == expected_str, f"Expected '{expected_str}', but got '{result}'"

def test_trig_term_create_random():
    term1 = TrigTerm.create_random()
    term2 = TrigTerm.create_random()
    print(f"\nRandomly created trig term 1: {term1}")
    print(f"Randomly created trig term 2: {term2}")
    assert term1.a != term2.a or term1.b != term2.b or term1.c != term2.c, "Randomly created trig terms had the same a, b, and c values"

def test_trig_term_mutate():
    term = TrigTerm(1, 1, 0, "sin")
    print(f"\nTrig mutate test, before mutate: {term}")
    term.mutate()
    print(f"Trig mutate test, after mutate: {term}")
    term.mutate()
    print(f"Trig mutate test, after second mutate: {term}")
    term.mutate()
    print(f"Trig mutate test, after third mutate: {term}")