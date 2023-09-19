from main import rpn_calculator
import pytest


def test_rpn_calculator_basic_operations(capsys, monkeypatch):
    # Test addition
    input_values = ["3 4 +", "q"]
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    rpn_calculator()
    captured = capsys.readouterr()
    assert "Current Stack: [7.0]\nFinal Stack: [7.0]" in captured.out

    # Test subtraction and multi-input operands
    input_values = ["10", "5 -", "q"]
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    rpn_calculator()
    captured = capsys.readouterr()
    assert (
        "Current Stack: [10.0]\nCurrent Stack: [5.0]\nFinal Stack: [5.0]\nCalculator has been terminated.\n"
        in captured.out
    )

    # Test multiplication and single input calculations
    input_values = ["6", "7", "*", "5", "1", "* *", "q"]
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    rpn_calculator()
    captured = capsys.readouterr()
    assert (
        "Current Stack: [6.0]\nCurrent Stack: [6.0, 7.0]\nCurrent Stack: [42.0]\nCurrent Stack: [42.0, 5.0]\nCurrent Stack: [42.0, 5.0, 1.0]\nCurrent Stack: [210.0]\nFinal Stack: [210.0]\nCalculator has been terminated.\n"
        in captured.out
    )

    # Test division
    input_values = ["20 4 /", "q"]
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    rpn_calculator()
    captured = capsys.readouterr()
    assert "Current Stack: [5.0]\nFinal Stack: [5.0]" in captured.out

    # Test floats
    input_values = ["3.5 4.5 +", "q"]
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    rpn_calculator()
    captured = capsys.readouterr()
    assert "Current Stack: [8.0]\nFinal Stack: [8.0]" in captured.out

    # Test multiple operations
    input_values = ["20 4 /", "5 6 7 +", "- *", "q"]
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    rpn_calculator()
    captured = capsys.readouterr()
    assert (
        "Current Stack: [5.0]\nCurrent Stack: [5.0, 5.0, 13.0]\nCurrent Stack: [-40.0]\nFinal Stack: [-40.0]\nCalculator has been terminated.\n"
        in captured.out
    )


def test_rpn_calculator_error_handling(capsys, monkeypatch):
    # Test division by zero
    input_values = ["5 0 /", "9 3 +", "q"]
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    rpn_calculator()
    captured = capsys.readouterr()
    assert (
        "Error: Division by zero\nCurrent Stack: [5.0, 0.0]\nCurrent Stack: [5.0, 0.0, 12.0]\nFinal Stack: [5.0, 0.0, 12.0]\nCalculator has been terminated.\n"
        in captured.out
    )

    # Test invalid input
    input_values = ["x 9 9 +", "q"]
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    rpn_calculator()
    captured = capsys.readouterr()
    assert (
        "Error: Invalid input 'x'\nCurrent Stack: [18.0]\nFinal Stack: [18.0]\nCalculator has been terminated.\n"
        in captured.out
    )

    # Test multiple errors input
    input_values = ["10 x +", "q"]
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    rpn_calculator()
    captured = capsys.readouterr()
    assert (
        "Error: Invalid input 'x'\nError: Not enough operands for operator '+'\nCurrent Stack: [10.0]\nFinal Stack: [10.0]\nCalculator has been terminated.\n"
        in captured.out
    )
