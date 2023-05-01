from expression import Expression
if __name__ == "__main__":
    expressions = [Expression(True) for _ in range(64)]
    for expression in expressions:
        print(expression._constant)
        print(expression._terms[0])