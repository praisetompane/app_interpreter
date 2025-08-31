from app_interpreter.interpreter import Interpreter

def test_app():
    interpreter = Interpreter()
    assert {1:1} == interpreter.evaluate("11 10 >=")