class VMInterpreter:
    def __init__(self):
        self.instructions = {
            "add": self.addVal,
            "mov": self.movVal,
            "print": self.printVal,
            "jnz": self.jumpNotZero,
        }
        self.registers = {}
        self.index=0

#Add the values of the registers x and y and store the result into the x register
    def addVal(self, x, y):
        if x not in self.registers or y not in self.registers:
            raise ValueError("Register does not exist")
            
        self.registers[x] = int(self.registers[x]) + self.registers[y]

#Copy the value of y (which could be a constant or the contents of a register) into register x
    def movVal(self, x, y):
        self.registers[x] = int(y)
        return

#Print the Unicode representation of the value in the register x to stdout (without a newline character)
    def printVal(self, x):
        if x not in self.registers:
            raise ValueError("Register does not exist")

        print(chr(self.registers[x]),end='')
        return

#jump to instruction y
    def jumpNotZero(self, x, y):
        if x.isdigit():
            if not y.lstrip("-").isdigit():
                raise ValueError("Invalid register")
            elif int(x) != 0:
                self.index = self.index + int(y) - 1
        else:
            if x not in self.registers:
                raise ValueError("Invalid register")
            else:
                if int(self.registers[x]) != 0:
                    self.index = self.index + int(y) - 1

    def run(self, code):
            lines = list(filter(None, code.split("\n")))
            while self.index < len(lines):
                parts = lines[self.index].strip().split(" ")
                try:
                    self.instructions[parts[0]](*parts[1:])
                    self.index += 1
                except:
                    raise ValueError("Unknown instruction")

interpreter = VMInterpreter()
input = open('input-2.asm','r').read()

interpreter.run(input)