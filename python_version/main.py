import operator
from token_handlers import handle_operator, handle_operand
from enums import HANDLED_OPERATORS as OPERATORS


def rpn_calculator():
    stack = []

    while True:
        expression = input(
            "Enter operand(s) and/or operator(s) (q to quit or c to clear): "
        )
        if expression.lower() == "q":
            break
        if expression.lower() == "c":
            stack.clear()
            continue

        tokens = expression.split()

        for token in tokens:
            if token in OPERATORS:
                handle_operator(token, stack)
            else:
                handle_operand(token, stack)

        if stack:
            print("Current Operand Stack:", stack)

    if stack:
        print("Final Operand Stack:", stack)
    print("Calculator has been terminated.")


if __name__ == "__main__":
    rpn_calculator()
