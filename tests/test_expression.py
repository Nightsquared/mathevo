import sys
sys.path.insert(0, '/Users/David/Documents/mathevo')
sys.path.insert(0, '/Users/David/Documents/mathevo/terms')

from expression import Expression
from terms import PolynomialTerm, ExponentialTerm
import pytest

def test_mutate():
    exp = Expression()
    exp.add_term(PolynomialTerm(-1, 2))
    print(f"\nExpression mutate test, starting expression: {exp}")
    for i in range(10):
        exp.mutate()
        print(f"Expression after mutate {i}: {exp}")