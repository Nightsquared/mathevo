import random
from terms import *
from typing import List
class Expression:
    def __init__(self, create_term = False, lower=-2, upper=2, steps=40):
        self._terms:List[Term] = []
        self._constant:float = 0

        #used for integral calculation
        self.lower = lower
        self.upper = upper
        self.steps = steps

        if create_term:
            self.add_term(self._create_random_term())

        self._calculate_constant()
            
    def __str__(self):
        expression_str = " + ".join(str(term) for term in self._terms) + ( ' + ' + str(round(self._constant, 2)) if self._constant > 0 else ' - ' + str(-round(self._constant, 2)))
        return expression_str
    
    def add_term(self, term):
        self._terms.append(term)

    def remove_term(self, term):
        if term in self._terms:
            self._terms.remove(term)
    
    def evaluate(self, x):
        '''
        Evaluates the constant for x, as the sum of the evaluation of each term plus the constant.
        '''
        expression_value = sum(term.evaluate(x) for term in self._terms) + self._constant
        return expression_value

    def _integrate(self):
        expression_integral = sum(term.integrate(self.lower, self.upper, self.steps) for term in self._terms)
        return expression_integral
    
    def _calculate_constant(self):
        '''
        Calculates the constant.
        The constant will be the negative of the sum of the integrals of each term between the given bounds
        '''
        self._constant = -self._integrate()
    
    def mutate(self, weights:List[float] = [.1, .1, .8]):
        """
        Mutate the expression by either adding, deleting, or mutating a term, based on the given weights.
        
        :param weights: A list of 3 float values representing the probabilities of adding, deleting, or mutating a term, respectively.
        """
        assert len(weights) == 3, "The weights list should have exactly 3 elements."
        
        choice = random.choices(["add", "delete", "mutate"], weights, k=1)[0]
        
        if choice == "add":
            new_term = self._create_random_term()
            self.add_term(new_term)
        elif choice == "delete":
            if len(self._terms) > 1:
                term_to_remove = random.choice(self._terms)
                self.remove_term(term_to_remove)
            else:
                self.mutate([weights[0] + weights[1], 0, weights[2]])
        elif choice == "mutate":
            term_to_mutate = random.choice(self._terms)
            if term_to_mutate.mutate():
                self.remove_term(term_to_mutate)
        else:
            raise ValueError(f"Invalid choice: {choice}")
        self._calculate_constant()

    def _create_random_term(self):
        """
        Create a new random term object by choosing from the available term subclasses and calling their respective create functions.
        """
        term_subclasses = {
            PolynomialTerm: PolynomialTerm.create_random,
            TrigTerm: TrigTerm.create_random,
            ExponentialTerm: ExponentialTerm.create_random
        }

        term_class = random.choice(list(term_subclasses.keys()))
        return term_subclasses[term_class]()