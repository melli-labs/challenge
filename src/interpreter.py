from typing import List

from utils import is_int

class CommandException(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(args)

class RegisterException(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Interpreter:
    
    def __init__(self) -> None:
        self.registers = {}
        self.current_line_num = 0
    
    def get_arg_value(self, arg):
        """Returns either constant or contents of register"""
        if is_int(arg):
            return int(arg)
        else:
            return self.registers[arg]
    
    def run_add_command(self, args: List[str]):
        """add command"""
        if len(args) != 2:
            raise CommandException("Incorrect number of arguments for `add` command")
        
        x = args[0]
        y = args[1]
        
        if x not in self.registers.keys():
            raise RegisterException("Incorrect register address")
        
        self.registers[x] += self.registers[y]
    
    def run_move_command(self, args: List[str]):
        """mov command"""
        if len(args) != 2:
            raise CommandException("Incorrect number of arguments for `mov` command")
        
        x = args[0]
        y = self.get_arg_value(args[1])
        
        self.registers[x] = y
        
    def run_print_command(self, args: List[str]):
        """print command"""
        if len(args) != 1:
            raise CommandException("Incorrect number of arguments for `print` command")
        
        x = args[0]
        
        if x not in self.registers.keys():
            raise RegisterException("Incorrect register address")
        
        print(chr(self.registers[x]), end='')
        
    def run_jump_command(self, args: List[str]):
        """jnz command"""
        if len(args) != 2:
            raise CommandException("Incorrect number of arguments for `jnz` command")
        
        x = self.get_arg_value(args[0])
        y = int(args[1])
        
        if x != 0:
            self.current_line_num += y
            self.current_line_num -= 1 # fix for step increasing after the command is executed
        
            
    def run_line(self, line: str):
        """Execute single line of code"""
        
        command, *args = line.replace("\n", "").split(" ")
        if command == "mov":
            self.run_move_command(args)
        elif command == "add":
            self.run_add_command(args)
        elif command == "print":
            self.run_print_command(args)
        elif command == "jnz":
            self.run_jump_command(args)

    
    def run(self, lines: List[str]):
        while self.current_line_num < len(lines):
            self.run_line(lines[self.current_line_num])
            self.current_line_num += 1            
