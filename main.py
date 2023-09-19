import operator

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def rpn_calculator():
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
            stack.append(int(token))
        elif token in OPERATORS:
            operand2, operand1 = stack.pop(), stack.pop()
            result = OPERATORS[token](operand1, operand2)
            stack.append(result)
        else:
            raise ValueError("Invalid token: {}".format(token))

    if len(stack) != 1:
        raise ValueError("Invalid expression")

    return stack[0]


if __name__ == "__main__":
    expression = input("Enter an RPN expression: ")
    try:
        result = rpn_calculator(expression)
        print("Result: {}".format(result))
    except ValueError as e:
        print("Error:", e)
