from typing import List

class CommandException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Interpreter:
    
    def __init__(self) -> None:
        self.registers = {}
        
    def run_add_command(self, args: List[str]):
        if len(args) != 2:
            raise CommandException()
        
        x = args[0]
        y = args[1]
        
        self.registers[x] += self.registers[y]
    
    def run_move_command(self, args: List[str]):
        if len(args) != 2:
            raise CommandException()
        
        x = args[0]
        y = args[1]
        if y.isdigit() or (y[0] in ["-","+"] and y[1:].isdigit()):
            y_value = int(y)
        else:
            y_value = self.registers[y]
        
        self.registers[x] = y_value
        
    def run_print_command(self, args: List[str]):
        if len(args) != 1:
            raise CommandException()
        
        x = args[0]
        
        print(chr(self.registers[x]), end='')
        
            
    def run_line(self, line: str):
        command, *args = line.replace("\n", "").split(" ")
        if command == "mov":
            self.run_move_command(args)
        if command == "add":
            self.run_add_command(args)
        if command == "print":
            self.run_print_command(args)

    
    def run(self, lines):
        for line in lines:
            self.run_line(line)

