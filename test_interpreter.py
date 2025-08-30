import sys
from interpreter import evaluate_expression

def test_addition():
    assert 5 == evaluate_expression("1 4 + ")

if __name__ == "__main__":
    test_addition()