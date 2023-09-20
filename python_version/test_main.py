from main import rpn_calculator
import pytest


@pytest.mark.parametrize(
    "input_value_list,captured_out",
    [
        (
            ["3 4       +", "q"],
            "Current Operand Stack: [7.0]\nFinal Operand Stack: [7.0]",
        ),  # Test addition and extra whitespace
        (
            ["10", "5 -", "q"],
            "Current Operand Stack: [10.0]\nCurrent Operand Stack: [5.0]\nFinal Operand Stack: [5.0]\nCalculator has been terminated.\n",
        ),  # Test subtraction and multi-input operands
        (
            ["6", "7", "*", "5", "1", "* *", "q"],
            "Current Operand Stack: [6.0]\nCurrent Operand Stack: [6.0, 7.0]\nCurrent Operand Stack: [42.0]\nCurrent Operand Stack: [42.0, 5.0]\nCurrent Operand Stack: [42.0, 5.0, 1.0]\nCurrent Operand Stack: [210.0]\nFinal Operand Stack: [210.0]\nCalculator has been terminated.\n",
        ),  # Test multiplication and single input calculations
        (
            ["20 4 /", "q"],
            "Current Operand Stack: [5.0]\nFinal Operand Stack: [5.0]",
        ),  # Test division
        (
            ["3.5 4.5 +", "q"],
            "Current Operand Stack: [8.0]\nFinal Operand Stack: [8.0]",
        ),  # Test floats
        (
            ["20 4 /", "5 6 7 +", "- *", "q"],
            "Current Operand Stack: [5.0]\nCurrent Operand Stack: [5.0, 5.0, 13.0]\nCurrent Operand Stack: [-40.0]\nFinal Operand Stack: [-40.0]\nCalculator has been terminated.\n",
        ),  # Test multiple operations
        (
            ["5 0 /", "9 3 +", "q"],
            "Error: Division by zero\nCurrent Operand Stack: [5.0, 0.0]\nCurrent Operand Stack: [5.0, 0.0, 12.0]\nFinal Operand Stack: [5.0, 0.0, 12.0]\nCalculator has been terminated.\n",
        ),  # Test division by zero
        (
            ["x 9 9 +", "q"],
            "Error: Invalid input 'x'\nCurrent Operand Stack: [18.0]\nFinal Operand Stack: [18.0]\nCalculator has been terminated.\n",
        ),  # Test invalid input
        (
            ["10 x +", "q"],
            "Error: Invalid input 'x'\nError: Not enough operands for operator '+'\nCurrent Operand Stack: [10.0]\nFinal Operand Stack: [10.0]\nCalculator has been terminated.\n",
        ),  # Test multiple errors input
    ],
)
def test_rpn_calculator_paths(capsys, monkeypatch, input_value_list, captured_out):
    input_values = input_value_list
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    rpn_calculator()
    captured = capsys.readouterr()
    assert captured_out in captured.out
