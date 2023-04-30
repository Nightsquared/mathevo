class Expression:
    def __init__(self):
        self.terms = []

    def add_term(self, term):
        self.terms.append(term)

    def __str__(self):
        expression_str = " + ".join(str(term) for term in self.terms)
        return expression_str