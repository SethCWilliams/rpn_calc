from main import rpn_calculator


def test_rpn_calculator():
    assert rpn_calculator("5 5 5 8 + + -") == -13
    assert rpn_calculator("5 9 1 - /") == 0.625
    assert rpn_calculator("-5 6 4 * -") == -29
    assert rpn_calculator("5") == 5
    assert rpn_calculator("-5") == -5
    assert rpn_calculator("5 7 3 29 * + -") == -89  # 3*29=87, 7+87=94, 5-94=-89
