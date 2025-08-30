from src.app_interpreter.interpreter import Evaluator

interpreter = Evaluator()


def test_addition():
    assert 5 == interpreter.evaluate_arithmetic("1 4 + ")


def test_file_processing():
    program_text = open("tests/app_interpreter/addition.txt").read()
    interpreter.evaluate_program(program_text)


if __name__ == "__main__":
    test_addition()
    test_file_processing()
