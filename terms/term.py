class Term:
    '''
    Abstract class
    '''
    def __str__(self):
        pass

    def evaluate(self, x):
        pass

    #calculate an approximate integral for this term between the lower and upper bounds.
    #I used the midpoint rule.
    def integrate(self, lower = -2, upper = 2, steps = 40):
        const = (upper - lower) / steps
        total = 0
        x = lower + const / 2
        while x < upper:
            total += self.evaluate(x)*const
            x += const
        return total
    
    @classmethod
    def create_random(self):
        pass

    def mutate(self):
        '''
        Randomly mutates a property in this term.
        If the result would be trivial, this function returns true to indicate it should be deleted.
        Otherwise, it returns false.
        '''
        pass