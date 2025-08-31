from src.app_interpreter.interpreter import Evaluator


def test_addition():
    interpreter = Evaluator()
    interpreter.evaluate_program("1 4 + ")
    assert {5:5} == interpreter.variables

def test_program_file_parsing():
    interpreter = Evaluator()
    program_text = open("tests/resources/addition.txt").read()
    interpreter.evaluate_program(program_text)
    assert {5: 5, 6: 6} == interpreter.variables


def test_addition_with_variables():
    interpreter = Evaluator()
    program_text = open("tests/resources/addition_variables.txt").read()
    interpreter.evaluate_program(program_text)
    assert {'x': 6, 'y': 11} == interpreter.variables

def test_subtraction():
    interpreter = Evaluator()
    program_text = open("tests/resources/subtraction.txt").read()
    interpreter.evaluate_program(program_text)
    assert {-3: -3} == interpreter.variables


def test_multiplication():
    interpreter = Evaluator()
    program_text = open("tests/resources/multiplication.txt").read()
    interpreter.evaluate_program(program_text)
    assert {8: 8} == interpreter.variables

def test_while_loop_truth_case():
    interpreter = Evaluator()
    program_text = open("tests/resources/while_truth_case.txt").read()
    interpreter.evaluate_program(program_text)
    assert {'n': 0} == interpreter.variables

def test_while_loop_false_case():
    interpreter = Evaluator()
    program_text = open("tests/resources/while_false_case.txt").read()
    interpreter.evaluate_program(program_text)
    assert {'n': 5, 'y': 10} == interpreter.variables

def test_factorial():
    interpreter = Evaluator()
    program_text = open("tests/resources/factorial.txt").read()
    interpreter.evaluate_program(program_text)
    assert {'n': 0, 'factorial': 120} == interpreter.variables

if __name__ == "__main__":
    test_addition()
    test_program_file_parsing()
    test_addition_with_variables()
    test_subtraction()
    test_multiplication()
    test_while_loop_truth_case()
    test_while_loop_false_case()
    test_factorial()
