class VirtualMachine:
    def __init__(self):
        self.registers = {}
        self.step = 0
        self.instructions = {
            "add": self.add,
            "mov": self.mov,
            "print": self.print_register,
            "jnz": self.jump_not_zero
        }
    # This function is used to add the values of the registers x and y and store the result into the x register
    def add(self, x, y):
        if x.isdigit():
            raise ValueError("Invalid instruction x should be a register")
        else:
            if x not in self.registers:
                raise ValueError(
                    "Invalid register {x} you have to implement it first")
            else:
                if y.isdigit():
                    self.registers[x] = int(self.registers[x])+int(y)
                else:
                    self.registers[x] = int(
                        self.registers[x])+int(self.registers[y])
    # This function used to copy the value of y into register x
    def mov(self, x, y):
        self.registers[x] = int(y)
    # This function is used to print the Unicode representation of the value in the register x without a newline character.
    def print_register(self, x):
        if x not in self.registers:
            raise ValueError("Invalid register")
        else:
            print(chr(self.registers[x]), end='')
    # This function assert the jump to the aimed adress
    def jump_not_zero(self, x, y):
        if x.isdigit():
            if not y.lstrip("-").isdigit():
                raise ValueError("Invalid register")
            elif int(x) != 0:
                self.step = self.step + int(y) - 1
        else:
            if x not in self.registers:
                raise ValueError("Invalid register")
            else:
                if int(self.registers[x]) != 0:
                    self.step = self.step + int(y) - 1
    # With this function the user is able to run the Virtual machine
    def run(self, code):
        code_lines = list(filter(None, code.split("\n")))
        while self.step < len(code_lines):
            parts = code_lines[self.step].strip().split(" ")
            try:
                self.instructions[parts[0]](*parts[1:])
                self.step += 1
            except:
                raise ValueError("Invalid instruction")


vm = VirtualMachine()

##############################################################
# Hier if you want to read the data direct from the asm file #
#  input-1.asm or input-2.asm                                #
##############################################################
# with open('input-2.asm','r') as asm_data:
#    vm.run(asm_data.read())

code_asm_1 = """
mov a 99
mov b 16
mov c 2
add b a
add c a
print b
print c
print a
mov b 15
add b a
print b
print c
mov c 17
add c a
print c
"""
code_asm_2 = """
mov s 0
mov d 0
mov a 80
mov b 804
mov c -1
add s a
add b c
jnz b -3
jnz d 3
mov d 1
jnz 1 -8
mov a 9484
print a
mov b 21
mov a -1
mov c 9472
print c
add b a
jnz b -2
mov a 9488
print a
mov a 10
print a
mov a 9474
print a
mov a 32
print a
mov a 89
print a
mov a 111
print a
mov a 117
print a
mov a 32
print a
mov a 97
print a
mov a 114
print a
mov a 101
print a
mov a 32
print a
mov a 116
print a
mov a 104
print a
mov a 101
print a
mov a 32
print a
mov a 98
print a
mov a 101
print a
mov a 115
print a
mov a 116
print a
mov a 32
print a
mov a 127942
print a
mov a 32
print a
mov a 9474
print a
mov a 10
print a
mov a 9492
print a
mov b 21
mov a -1
mov c 9472
print c
add b a
jnz b -2
mov a 9496
print a
mov a 10
print a
mov a 84
print a
mov a 104
print a
mov a 101
print a
mov a 32
print a
mov a 115
print a
mov a 111
print a
mov a 108
print a
mov a 117
print a
mov a 116
print a
mov a 105
print a
mov a 111
print a
mov a 110
print a
mov a 32
print a
mov a 105
print a
mov a 115
print a
mov a 58
print a
mov a 32
print a
print s
mov a 10
print a
"""
vm.run(code_asm_2)
