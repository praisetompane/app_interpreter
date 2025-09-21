from app_interpreter.control_unit import ControlUnit
import argparse
from app_interpreter.arithmetic_logic_unit import ArithmeticLogicUnit


def main() -> str:
    parser = argparse.ArgumentParser(
        "python src/app_interpreter/app.py ./tests/resources/factorial.txt"
    )

    parser.add_argument("program_file")

    args = parser.parse_args()

    program_text = open(args.program_file).read()

    interpreter = ControlUnit(ArithmeticLogicUnit())

    return interpreter.execute(program_text)


if __name__ == "__main__":
    print(main())
