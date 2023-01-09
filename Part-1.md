# Part 1

Our goal is to implement an interpreter for a simple virtual machine. No worries, at first this might sound more complicated than it really is! 

The registers in our little virutal machine hold integer value, and the registers are identified by a string (every valid string identifies a different register). The assembly language for this virtual machine is pretty simply. It includes the following instructions:

* `add x y`: Add the values of the registers `x` and `y` and store the result into the `x` register
* `mov x y`: Copy the value of `y` (which could be a constant or the contents of a register) into register `x`
* `print x`: Print the unicode representation of the value in the register `x` to stdout (without a newline character).

> *Note*
> Constants are always integers and can be positive or negative.

In case the interpreter get an invalid instruction it, the execution should be halted and an appropriate error message should be shown.

For the following input

```
mov a 104
mov b 1
add b a
print a
print b
```

you interpreter, should output:

```
hi
```

Let's go!
