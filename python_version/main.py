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
            if token in OPERATORS:
                if len(stack) < 2:
                    print(f"Error: Not enough operands for operator '{token}'")
                    continue
                operand2, operand1 = stack.pop(), stack.pop()
                try:
                    result = OPERATORS[token](operand1, operand2)
                    stack.append(result)
                except ZeroDivisionError:
                    print("Error: Division by zero")
                    stack.append(operand1)
                    stack.append(operand2)
            else:
                try:
                    # Try converting the token to a float
                    value = float(token)
                    stack.append(value)
                except ValueError:
                    print(f"Error: Invalid input '{token}'")
                except Exception as e:
                    print("Error:", e)

        if stack:
            print("Current Stack:", stack)

    if stack:
        print("Final Stack:", stack)
    print("Calculator has been terminated.")


if __name__ == "__main__":
    rpn_calculator()
