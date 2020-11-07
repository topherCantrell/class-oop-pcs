# Write a "program" for a "computer"

Developers wait patiently in their cubes for their bosses to come by and give them a very
specific problem to write code to solve. They create this program in exchange for pizza
and libations.

Let's take a simple problem for example:

Ms. Crump teaches 3rd grade. Each student in the class has a set of ten grades for the school year.
Write a program to compute the average of the grades.

Already the machinery in your head is turning, isn't it? We'll need a data structure of some kind to
hold the list of grades -- probably a simple array, and we'll access the grades by index. 

We'll need a loop -- we need to visit each element of the array (each grade) one by one and add it up. 

We'll probably need some variables -- the current index of the array we are visiting and the running tally
as we add them up.

And finally we'll need the division -- tally by number of elements.

What about error checking? What if Ms. Crump runs your program on an empty list of grades? It's OK if you
didn't think about that up front. One of your test cases would have been an empty list. This is why we
write test cases: to catch the things we didn't think of.

# Compiling

These are the things they teach you basic computer science class: loops and conditions and variables.

Your program might look something like this in python (but probably much shorter and cleaner):

```python
grades = [75,66,84,90,92,100,38,73,22,95]
count = 10

i = 0
total = 0
while True:
    if i >= count:
        break
    v = grades[i]
    total = total + v
    i = i + 1    
    
avg = total / count

print(avg)
```

The computer hardware doesn't understand these high-level instructions. It has a set of very primitive instructions,
and the compiler's job is to translate these high-levels you understand into the low-levels that the hardware
understands. 

This is just a pretend instruction set -- not a real processor.

```
    set R1 to 0 ; using R1 as i
    set R2 to 0 ; using R2 as total
  
top_of_loop:
    compare R1 to R6 ; using R6 as count
    goto bottom_of_loop if last math operation did not borrow
    set R3 to R4[R1] ; using R3 as v, using R4 as pointer to grades
    set R2 to R2 + R3
    set R1 to R1 + 1
    goto top_of_loop
  
bottom_of_loop:
    set R1 = R2 / R6 ; reusing R1 as average
```

The lines with colons are not instructions. They are labels that identify GOTO destinations. That's right,
the low level hardware is all about GOTOs even though you have been taught they are evil. For instance,
"goto top_of_loop" is a GOTO back up to the "compare R1 to R6" instruction.

Our pretend processor has a number of internal registers R1 to R8 that the compiler maps to our variables.
This is a primary job of the compiler: mapping our variables and data structures to memory addresses and/or
internal registers.

You can write your program using these low-level hardware instructions. We used to have to do that. This is
what we call "assembly language". Of course, the hardware doesn't understand the text -- it needs numbers.

The assembler converts these mnemonics to bytes. Different instructions could have a different number of bytes.
The assembler lays these bytes out in memory. Here, we'll say 1000 for example.


```
1000: 76 35 00     set i to 0
1003: 76 36 00     set total to 0
  
top_of_loop:
1006: 90 35 36     compare i to count
1009: 51 --        goto bottom_of_loop if last math operation did not borrow
1011: 91 36 22 40  set v to grades[i]
1015: 32 10 20     set total to total + v
1018: 88           set i to i + 1
1019: 52 --        goto top_of_loop
  
bottom_of_loop:
1027: 76 37 88     set avg = total / count
```

The numbers on the left are the opcodes for the instructions on the right. Each line here is shown with
the starting memory location for the bytes.

Notice the "--" at 1009. When the compiler is first building these instructions, it doesn't know how far
away the label is going to be. Will it be 10 bytes? 200 bytes? The instruction includes that piece of
data, but the compiler doesn't know what to put there until it has all the instructions.

The first pass through the code figures out where the instructions go. The second pass fills in the destinations.

```
1000: 76 35 00     set i to 0
1003: 76 36 00     set total to 0
  
top_of_loop:
1006: 90 35 36     compare i to count
1009: 51 42        goto bottom_of_loop (1027) if last math operation did not borrow
1011: 91 36 22 40  set v to grades[i]
1015: 32 10 20     set total to total + v
1018: 88           set i to i + 1
1019: 52 93        goto top_of_loop (1006)
  
bottom_of_loop:
1027: 76 37 88     set avg = total / count
```
