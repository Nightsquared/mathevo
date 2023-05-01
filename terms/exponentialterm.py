from term import Term
import math
import random

class ExponentialTerm(Term):
    def __init__(self, a, b):
        '''
        a * b^x
        '''
        self.a = a
        self.b = b

    def __str__(self):
        term_str = f"{round(self.a, 2)}({round(self.b, 2)}^x)" if self.a != 1 and self.a != -1 else f"{round(self.b, 2)}^x" if self.a == 1 else f"-{round(self.b, 2)}^x"
        return term_str

    def evaluate(self, x):
        return self.a * (self.b ** x)

    @classmethod
    def create_random(cls):
        a = random.uniform(-10, 10)
        b = random.uniform(0, 2)
        return cls(a, b)

    def mutate(self):
        mutation_choice = random.choice(["a", "b"])

        if mutation_choice == "a":
            self.a *= random.uniform(-4, 4)
        elif mutation_choice == "b":
            self.b *= random.uniform(0, 2)
        else:
            raise ValueError(f"Invalid mutation choice: {mutation_choice}")

        return self.a == 0 or self.b == 0