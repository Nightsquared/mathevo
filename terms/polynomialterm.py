from term import Term
import random
class PolynomialTerm(Term):
    def __init__(self, a=1, b=1):
        '''
        ax^b
        '''
        self.a = a
        self.b = b

    def __str__(self):
        if self.a == 1:
            term_str = "x"
        elif self.a == -1:
            term_str = "-x"
        else:
            term_str = f"{round(self.a, 2)}x"
        
        if self.b != 1:
            term_str += f"^{round(self.b, 2)}"
        return term_str
    
    def evaluate(self, x):
        return self.a * (x ** self.b)
    
    @classmethod
    def create_random(cls):
        a = random.uniform(-10, 10)
        b = random.randint(-5, 5)
        return cls(a, b)
    
    def mutate(self):
        mutation_choice = random.choice(["a", "b"])

        if mutation_choice == "a":
            self.a *= random.uniform(-4, 4) 
        elif mutation_choice == "b":
            self.b += random.randint(-3, 3)
        else:
            raise ValueError(f"Invalid mutation choice: {mutation_choice}")
        
        return self.a == 0 or self.b == 0
    
