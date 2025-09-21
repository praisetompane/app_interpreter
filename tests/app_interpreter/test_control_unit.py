from app_interpreter.control_unit import ControlUnit
from app_interpreter.arithmetic_logic_unit import ArithmeticLogicUnit


def test_addition():
    interpreter = ControlUnit(ArithmeticLogicUnit())
    interpreter.execute("1 4 + ")
    assert {5: 5} == interpreter._general_purpose_registers


def test_program_file_parsing():
    interpreter = ControlUnit(ArithmeticLogicUnit())
    program_text = open("tests/resources/addition.txt").read()
    interpreter.execute(program_text)
    assert {5: 5, 6: 6} == interpreter._general_purpose_registers


def test_addition_with__general_purpose_registers():
    interpreter = ControlUnit(ArithmeticLogicUnit())
    program_text = open("tests/resources/addition_variables.txt").read()
    interpreter.execute(program_text)
    assert {"x": 6, "y": 11} == interpreter._general_purpose_registers


def test_subtraction():
    interpreter = ControlUnit(ArithmeticLogicUnit())
    program_text = open("tests/resources/subtraction.txt").read()
    interpreter.execute(program_text)
    assert {-3: -3} == interpreter._general_purpose_registers


def test_multiplication():
    interpreter = ControlUnit(ArithmeticLogicUnit())
    program_text = open("tests/resources/multiplication.txt").read()
    interpreter.execute(program_text)
    assert {8: 8} == interpreter._general_purpose_registers


def test_while_loop_truth_case():
    interpreter = ControlUnit(ArithmeticLogicUnit())
    program_text = open("tests/resources/while_truth_case.txt").read()
    interpreter.execute(program_text)
    assert {"n": 0} == interpreter._general_purpose_registers


def test_while_loop_false_case():
    interpreter = ControlUnit(ArithmeticLogicUnit())
    program_text = open("tests/resources/while_false_case.txt").read()
    interpreter.execute(program_text)
    assert {"n": 5, "y": 10} == interpreter._general_purpose_registers


def test_factorial():
    interpreter = ControlUnit(ArithmeticLogicUnit())
    program_text = open("tests/resources/factorial.txt").read()
    interpreter.execute(program_text)
    assert {"n": 0, "factorial": 120} == interpreter._general_purpose_registers


if __name__ == "__main__":
    test_addition()
    test_program_file_parsing()
    test_addition_with__general_purpose_registers()
    test_subtraction()
    test_multiplication()
    test_while_loop_truth_case()
    test_while_loop_false_case()
    test_factorial()
