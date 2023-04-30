class Term:
    '''
    Abstract class
    '''
    def __str__(self):
        pass

    def evaluate(self, x):
        pass

    def integrate(self, lower = -2, upper = 2, steps = 40):
        const = (upper - lower) / steps
        total = 0
        x = lower + const / 2
        while x < upper:
            total += self.evaluate(x)*const
            x += const
        return total