# Part 1

Our goal is to implement an interpreter for a simple virtual machine. No worries, at first this might sound more complicated than it is! 

The registers in our little virtual machine hold integer values, and the registers are identified by a string (every valid alphabetic string identifies a different register). The assembly language for this virtual machine is pretty simple. It includes the following instructions:

* `add x y`: Add the values of the registers `x` and `y` and store the result into the `x` register
* `mov x y`: Copy the value of `y` (which could be a constant or the contents of a register) into register `x`
* `print x`: Print the Unicode representation of the value in the register `x` to stdout (without a newline character).

> **Note**
> Constants are always integers and can be positive or negative.

In case the interpreter gets an invalid instruction, the execution should be halted and an appropriate error message should be shown.

**Example:**

For the following input

```
mov a 9999
mov b -10
add a b
print a
mov a 10
print a
```

your interpreter should output:

```
✅
```

You need to run the instructions in the `input-1.asm` to obtain the decryption password for `Part-2.md.encrypted` (see [README.md](README.md) for more details).

