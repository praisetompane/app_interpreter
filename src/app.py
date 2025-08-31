from app_interpreter.interpreter import Interpreter
import argparse

def main():
    parser = argparse.ArgumentParser("python src/app_interpreter/app.py ./tests/resources/factorial.txt")
    parser.add_argument("program_file")

    args = parser.parse_args()
    program_text = open(args.program_file).read()

    interpreter = Interpreter()
    return interpreter.evaluate(program_text)

if __name__ == "__main__":
    print(main())