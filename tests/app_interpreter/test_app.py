from app_interpreter.control_unit import ControlUnit
from app_interpreter.arithmetic_logic_unit import ArithmeticLogicUnit


# TODO: write CLI app test
def test_app():
    interpreter = ControlUnit(ArithmeticLogicUnit())
    assert {1: 1} == interpreter.execute("11 10 >=")
