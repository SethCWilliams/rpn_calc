import operator

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def rpn_calculator():
    stack = []

    while True:
        expression = input("Enter operand(s) and/or operator(s) (q to quit): ")

        if expression.lower() == "q":
            break

        tokens = expression.split()

        for token in tokens:
            try:
                if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                    stack.append(float(token))
                elif token in OPERATORS:
                    if len(stack) < 2:
                        print(
                            "Error: Not enough operands for operator '{}'".format(token)
                        )
                        continue
                    operand2, operand1 = stack.pop(), stack.pop()
                    result = OPERATORS[token](operand1, operand2)
                    stack.append(result)
                else:
                    print("Error: Invalid input '{}'".format(token))
            except Exception as e:
                print("Error:", e)
        if len(stack) > 0:
            print("Current Result:", stack[-1])

    print("Calculator has been terminated.")


if __name__ == "__main__":
    rpn_calculator()
