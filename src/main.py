import sys

from interpreter import Interpreter


if __name__ == "__main__":
    input_file_path = sys.argv[1]
    
    with open(input_file_path, "r") as file:
        lines = file.readlines()

    interpreter = Interpreter()
    interpreter.run(lines)