# Islands of Data and Code

Programming is an intricate dance between data and code. Variables and code-flow, arrays and functions, 
data structures and algorithms -- these are the two sides of the programming coin, and you deal with them 
in any programming language you use. Object Oriented Programming is a way to keep related data and 
code neatly coupled in little bundles.

## Ms. Crump

Developers wait patiently in their cubes for their bosses to come by and give them a very
specific problem to write code to solve. They create this program in exchange for pizza
and libations.

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

These are the things they teach you basic computer science class: loops and conditions and variables.

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

These lines translate to instructions for the hardware. 

## Structured Programming

Python lets us put statements right out in the "global" scope, but
other languages require us to to place code within functions. (And python code is usually organized into functions).

Code lives within functions that take parameters and return values. This is part "Structured" programming (not to 
be confused with structures), which emerged in the late 1950s.

We can refactor our global code into a reusable function that can be used on any list of grades. It is no longer tied to
Bobby".

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

## Related Functions

In a real-sized application, there are usually lots of functions that go with a data structure. Along with
our `get_average` we have functions to make our life easier: get the number of failing grades, get the
highest grade, and so forth. These functions are all related in that they take a pointer to the data
target data structure they work on. In all the functions below, the pointer to the structure is the first
parameter.

```python
def get_average(grades):
    # Code here
    return 75.5

def get_number_fails(grades):
    # Code here
    return 3

def get_highest_grade(grades):
    # Code here
    return 90

def get_grade(grades, index):
    return grades[index]

def set_grade(grades, index, value):
    grades[index] = value

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

Kind of like the passive voice. The car was driven by Paul. The burger was eaten by Pat. The focus is on the verb.

Switch around to say Paul drove the car. Pat ate the burger. The focus is on the noun.

TODO add other functions. Code increases.

TODO now make a datastructure -- name + grades. Structures increases.


  - next add functions (routines)  and data (structures)
  - OO is about organizing these routines -- and keeping them together with their data
  
OO is about organizing a large number of functions and structures.
small programs -- tools -- don't require a great deal of overall structure. 
OO makes more sense -- easier to understand -- with large systems. Which can be challenging in a classroom.

Program to get the average/lowest/highest for a list of grades: easy. Requires loops and algorithms and if
statements -- standard entry-level CS stuff.

Show array of floats. Get average, Get lowest/highest. Main function. How to enhance for multiple tests. What
if tests are more than a list of grades? (date topic). Add self parameter.

schOOl (see what I did there?)

  - Test
    - Get average
    - Get lowest/highest
    - Attributes: Get/set the date/topic
    
  - Student
    - Attributes: Get/set name/phone (permissions here)
    - Get number of absences
    - Mark absence
      
  - Class
    - Add students and tests
    - Print report cards