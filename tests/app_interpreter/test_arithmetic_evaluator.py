from app_interpreter.arithmetic_evaluator import ArithmeticEvaluator

arithmetic_expression_evaluator = ArithmeticEvaluator()

def test_addition():
    assert 6 == arithmetic_expression_evaluator.evaluate("5 1 +", {})

def test_subtraction():
    assert 10 == arithmetic_expression_evaluator.evaluate("11 1 -", {})

def test_multiplication():
    assert 110 == arithmetic_expression_evaluator.evaluate("11 10 *", {})

def test_dvision():
     assert 1.1 == arithmetic_expression_evaluator.evaluate("11 10 /", {})

def test_arithmetic_with_variables():
    assert 51 == arithmetic_expression_evaluator.evaluate("x 1 +", {'x': 50})

def test_equality():
    assert 1 == arithmetic_expression_evaluator.evaluate("11 10 >=", {})

def test_unsupported_operator():
    try:
        arithmetic_expression_evaluator.evaluate("11 10 >", {})
    except NotImplementedError as e:
        assert e.args[0] == "Provided operator > is not supported."