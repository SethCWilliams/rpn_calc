from enums import HANDLED_OPERATORS as OPERATORS


def handle_operator(token, stack):
    if len(stack) < 2:
        print(f"Error: Not enough operands for operator '{token}'")
        return
    operand2, operand1 = stack.pop(), stack.pop()
    try:
        result = OPERATORS[token](operand1, operand2)
        stack.append(result)
    except ZeroDivisionError:
        print("Error: Division by zero")
        stack.append(operand1)
        stack.append(operand2)


def handle_operand(token, stack):
    try:
        value = float(token)
        stack.append(value)
    except ValueError:
        print(f"Error: Invalid input '{token}'")
    except Exception as e:
        print("Error:", e)
