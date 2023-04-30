from term import Term

class PolynomialTerm(Term):
    def __init__(self, a=1, b=1):
        '''
        ax^b
        '''
        self.a = a
        self.b = b

    def __str__(self):
        term_str = f"{self.coefficient}{self.variable}"
        if self.exponent != 1:
            term_str += f"^{self.exponent}"
        return term_str
    
    def evaluate(self, x):
        return self.a * (x ** self.b)
    
