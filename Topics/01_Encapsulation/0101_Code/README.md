# Islands of Data and Code

Programming is an intricate dance between data and code. Variables and code-flow, arrays and functions, 
data structures and algorithms -- these are the two sides of the programming coin, and you deal with them 
in any programming language you use. Object Oriented Programming is a way to keep related data and 
code neatly coupled in little bundles.

## Ms. Crump

Let's take a simple problem for example:

![](crump.jpg)

Ms. Crump teaches 3rd grade. Each student in the class has a set of ten grades for the school year.
Write a program to compute the average of the grades for her.

Already the machinery in your head is turning, isn't it? We'll need a data structure of some kind to
hold the list of grades -- probably a simple array, and we'll access the grades by index. 

We'll need a loop -- we need to visit each element of the array (each grade) one by one and add it up. 

We'll probably need some variables -- the current index of the array we are visiting and the running sum
as we add them up.

And finally we'll need the division -- sum by number of elements.

What about error checking? What if Ms. Crump runs your program on an empty list of grades? It's OK if you
didn't think about that up front. One of your test cases would have been an empty list. This is why we
write test cases: to catch the things we didn't think of.

This is what you probably think about when someone asks you about "programming". These These are the things 
they teach you basic computer science class: loops and conditions and variables.

Your program might look something like this in python (but probably much shorter and cleaner):

```python
bobby = [75,66,84,90,92,100,38,73,22,95]
count = 10

i = 0
total = 0

while i<count:    
    v = bobby[i]
    total = total + v
    i = i + 1    
    
avg = total / count

print(avg)
```

Python might not be your favorite language, but this example looks amazingly similar in whatever language you pick.
In "whatever" language, the code naturally flows from top to bottom unless it runs into a loop (like the "while" in 
this example). There are variables like "i" and "v" that hold temporary results. There are math expressions, 
and there are calls to other functions/routines like "print".

## Structured Programming

Python lets us put statements right out in the "global" scope, but other languages require us to to place code 
within functions. (And python code is usually organized into functions).

Generally, code lives within functions. These functions can take incoming parameters and they can return values. 
This is a very old concept that that emerged with "Structured Programming" (not to be confused with structures)
in the late 1950s.

We can refactor our global code into a reusable function that can be used on any list of grades. It is no longer 
tied to "Bobby".

```python
def get_average(grades):
    count = len(grades)

    i = 0
    total = 0
    
    while i<count:    
        v = grades[i]
        total = total + v
        i = i + 1    
        
    avg = total / count
    
    return avg
    
jan = [100,100,80,95,100,90,92,84,98,100]
bobby = [75,66,84,90,92,100,38,73,22,95]

result = get_average(bobby)

print(result)
```

The syntax for defining functions, parameters, and returns is a little different from language to language. But
the concept is the same -- it is a core concept in all modern languages.

## Related Functions

In a real-sized application, there are usually lots of functions that work on the same data structure. Our
data structure is simple here -- just a list of numbers. But even so, we have other helper functions
to make our life easier. Along with `get_average` we might have:
  - `get_highest_grade` get the highest grade
  - `get_lowest_grade` get the lowest grade
  - `get_number_fail_grades` get the number of failing grades
  - `sort_grades` sort the grades in ascending order

These functions are all related in that they take a pointer to the target data structure they work on. In all the 
functions below, the pointer to the structure is the first parameter.

```python
def get_average(grades):
    # Code here
    return 75.5

def get_number_fail_grades(grades):
    # Code here
    return 3

def get_highest_grade(grades):
    # Code here
    return 90

def get_grade(grades, index):
    return grades[index]

def set_grade(grades, index, value):
    grades[index] = value
```

What about the `get_grade` and `set_grade` functions? Are they useful? They allow us to get and set individual 
grades within the array or grades. But couldn't we do that directly on the data structure without having to go
through a function?

```python
# Use the function like this:

set_grade(bobby,8,50)

# But we could just do:

bobby[8] = 50
```

Suppose there are rules we must enforce like "no negative grades" or "no grades over 100". If other code is
setting the data directly, we can only hope they know and enforce the rules. But we can't make them.

If we force other code to go through our functions, then we can code the rules into the functions and prevent
other code from messing up the data. This "other code" is rarely malicious. Rather it is just plain buggy.

This concept of "hiding behind code" is called Encapsulation, and it is one of the cornerstones of OO
programming. We'll have much more to say about it soon.

```python
jan = [100,100,80,95,100,90,92,84,98,100]    
bobby = [75,66,84,90,92,100,38,73,22,95]

print( get_average(jan) )

print( get_highest_grade(jan) )

v = get_grade(jan, 8)
set_grade(bobby, 8, v)

set_grade(bobby, 7, get_grade(jan, 7))

print( get_grade(bobby, 8) )

print( get_number_fails(bobby) )
```
