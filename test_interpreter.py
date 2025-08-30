from src.app_interpreter.interpreter import Evaluator


def test_addition():
    interpreter = Evaluator()
    assert 5 == interpreter.evaluate_arithmetic("1 4 + ")


def test_program_file_parsing():
    interpreter = Evaluator()
    program_text = open("tests/app_interpreter/addition.txt").read()
    interpreter.evaluate_program(program_text)
    assert {5: 5, 6: 6} == interpreter.variables


def test_addition_with_variables():
    interpreter = Evaluator()
    program_text = open("tests/app_interpreter/addition_variables.txt").read()
    interpreter.evaluate_program(program_text)
    assert {'x': 6, 'y': 11} == interpreter.variables


if __name__ == "__main__":
    test_addition()
    test_program_file_parsing()
    test_addition_with_variables()
