import sys
from xml.dom import IndexSizeErr

from interpreter import Interpreter

if __name__ == "__main__":
    try:
        input_file_path = sys.argv[1]
    except IndexError as e:
        print("ERROR: You have to provide an input file as an argument")
        quit()
    
    with open(input_file_path, "r") as file:
        lines = file.readlines()

    interpreter = Interpreter()
    interpreter.run(lines)