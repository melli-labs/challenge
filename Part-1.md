# Part 1

Our goal is to write an interpreter for a assembly language of a simple virtual machine. No worries, at first this might sound more complicated than it really is! The virutal machine has only registers and no dedic

infinite number of registers, every string is a valid register.

The assembly language includes the following instructions:

`add x y`: Add the values of the registers `x` and `y` and store the result into the `x` register
`mov x y`: Copy the value of `y` (which could be a constant or the contents of a register) into register `x`
`print x`: Print the unicode representation of the value in the register `x` to stdout.

Todo: Reword. Constants are always integers (positive or negative). Register names are alphabetical (letters only). 

In case the interpreter get an invalid instruction it, the execution should be halted and an appropriate error message should be shown.

Example:

```
mov a 104
mov b 1
add b a
print a
print b
```

Should output:

```
hi
```
