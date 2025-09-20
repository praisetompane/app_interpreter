from app_interpreter.arithmetic_logic_unit import ArithmeticLogicUnit

alu = ArithmeticLogicUnit()


def test_addition():
    assert 6 == alu.evaluate("5 1 +", {})


def test_subtraction():
    assert 10 == alu.evaluate("11 1 -", {})


def test_multiplication():
    assert 110 == alu.evaluate("11 10 *", {})


def test_dvision():
    assert 1.1 == alu.evaluate("11 10 /", {})


def test_arithmetic_with_variables():
    assert 51 == alu.evaluate("x 1 +", {"x": 50})


def test_equality():
    assert 1 == alu.evaluate("11 10 >=", {})


def test_unsupported_operator():
    try:
        alu.evaluate("11 10 >", {})
    except NotImplementedError as e:
        assert e.args[0] == "Provided operator > is not supported."
