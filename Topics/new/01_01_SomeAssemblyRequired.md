
multi-language ... see the first language. learn how things work under the covers and why all languages
lead to the same constructs. How OO evolved and how the mechanisms work. Any quirks you can explain
when you think at this level.

Memory. Array of bytes indexed by numerical address starting at 0. Read this value from memory 123
and write that value to memory 444. This is the CPUs entire view of the world ... the address/data
bus.

CPU understands a set of primitive instructions. Like load internal register A with memory 123.
Add the value 44 to A. Store the register A to memory 444.

These instructions read from memory. A "program counter" points to the next instruction. The CPU
fetches 1 or more bytes (however many bytes are in the instruction) and then executes the instruction.
Instructions are stored sequentially. The CPU moves through the addresses one by one.

Jump instruction load the program counter with a new value.

Show simple program. Talk through it. How it would look in python. Code is just a list of binary numbers.

0100: 12 01 23  LDA  123
                ADDA #1
                STA  123
                JMP  0100

Our compilers convert high level instructions to these built ins. Keeps up with addresses (for
code jumps and memory for variables). Give names to addresses (subroutine names and variables).
Easier for us to understand. Compiler does the math.

Different processors have different primitive instructions. This is why you can't take a program from
one machine and run it on another. Motorola 6800 0 in the PowerBook 100 understands different instructions
than the Intel i7 processor in my PC now.

Show same program on different processors. Opcodes are different. Mnemonics are different. Compiler 
hides all this for you converting your program to whatever processor you want. Except there
are challenges. Registers have different sizes. The A register on the 6502 is 8 bits (0-255).
The A register on the 6809 is 8 bits, but the X register is 16 bits. The AX register on the old 8086
computers is 16 bits, but it also has an EAX in 80386 protected mode that holds 32 bits.

On an 80386 your variable X can hold up to 2^32. But on a 6809, it only holds up to 255. Your programs
might not run as expected when compiled on other architectures. The language is "similar", but you 
still have to know your processor/computer specs for C.

Wouldn't it be nice if all were the same? Make our lives as programmers easier (and boring).

Java gave us the "virtual machine". It simulates a cpu ... fetching instructions byte by byte but
a program interprets the opcodes instead of the hardware itself. You could write your own
language. "01 xx xx" means load and the you write the python to interpret that. Show an easy
example. These domain specific languages are not new ... the sound boards in the old arcade games. DSL.

This virtual machine is then implemented in the native instructions of the different processors. Now the
register sizes are fixed. The endianness is fixed. Opcodes are the same.

Show some java disassembly. Some Python disassembly. V8 is compiled.

Does a good job of hiding the hardware, but still leaks through. Threading, processes, operating resources
like window objects, buttons, etc.

So that's where we are. VM languages available for portable, quick-to-write code. Use native compiled
languages (Fortran, C, Go) when you need the speed ... but have to wrangle the processor details.

The languages can be quite different, but ultimately that translate into these primitive instructions
for the processors. And those instructions are basically the same among all processors. Our
programming concepts are thus portable between languages and hardware.


         