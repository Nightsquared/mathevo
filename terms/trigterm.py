from term import Term
import math

class TrigTerm(Term):
    def __init__(self, a, b, c, trig_function):
        '''
        atrig_function(bx+c)
        '''
        self.a = a
        self.b = b
        self.c = c
        self.trig_function = trig_function

    def __str__(self):
        term_str = f"{self.a}{self.trig_function}({self.b}x + c)"
        return term_str
    
    def evaluate(self, x):
        angle = self.b * x + self.c
        if self.trig_function == "sin":
            trig_value = math.sin(angle)
        elif self.trig_function == "cos":
            trig_value = math.cos(angle)
        elif self.trig_function == "tan":
            trig_value = math.tan(angle)
        else:
            raise ValueError(f"Unsupported trigonometric function: {self.trig_function}")

        return self.a * trig_value