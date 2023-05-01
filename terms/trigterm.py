from term import Term
import math
import random
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
        a_str = "" if self.a == 1 else "-" if self.a == -1 else str(round(self.a, 2))
        b_str = "" if self.b == 1 else "-" if self.a == -1 else str(round(self.b, 2))
        c_str = "" if self.c == 0 else f" + {math.degrees(self.c):.0f}°" if self.c > 0 else f" - {-math.degrees(self.c):.0f}°"
        
        term_str = f"{a_str}{self.trig_function}({b_str}x{c_str})"
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
    
    @classmethod
    def create_random(cls):
        a = random.uniform(-10, 10)
        b = random.uniform(-5, 5)
        c = random.uniform(-math.pi, math.pi)
        trig_function = random.choice(["sin", "cos", "tan"])
        return cls(a, b, c, trig_function)

    def mutate(self):
        mutation_choice = random.choice(["a", "b", "c", "trig_function"])

        if mutation_choice == "a":
            self.a *= random.uniform(-10, 10)
        elif mutation_choice == "b":
            self.b *= random.uniform(-4, 4)
        elif mutation_choice == "c":
            self.c += random.uniform(-math.pi/4, math.pi/4)
        elif mutation_choice == "trig_function":
            self.trig_function = random.choice(["sin", "cos", "tan"])
        else:
            raise ValueError(f"Invalid mutation choice: {mutation_choice}")

        return self.a == 0 or self.b == 0