# Using Objects

The memory in your computer is a vast collection of functions and data. Programming is an intricate dance between this data and code.

Functions are where you write "code". Computer "instruction" are what you generally think of when you hear the word "programming". 
Within a function, you list out primitive instructions for the computer to blindly follow: "add one to A", then "print A", 
then "if A is less than 20, go back to the start of the list".

Once you have coded up a function, you can call it from another function. Thus functions resuse each other to build up more
and more complex functions.

The computer's memory is also where you store information (data). Essentially, a computer's memory is just a long list of storage
cells accessed by numerical index (address). You read the value from location 2. You write a value to location 64233. 

Memory is surprisingly primitive. A memory location can only hold a single, numerical (integer) value with a maximum value.
But we can group a series of locations together to form "structures" of more complex data. And we combine primitive structures 
together to form even more complex data structures.

For a long time in our programming history, functions and data were kept separated from one another. Your code was over here.
And your data was over there.



You are listing out 
instructions for the computer to follow one by one. A function 


Variables and code-flow, arrays and functions, data structures and algorithms -- these are the two sides of the programming coin, 
and you deal with them in any programming language you use. Object Oriented Programming is a way to keep related data and code 
neatly coupled in little bundles.

Functions are made from lines of code. Functions are lists
of instructions, and they can be somewhat primitive: 
  - Print the message "Hello"
  - Add one to variable A
  - If variable A is less than 20, go back to the first instruction
  - Print "Done"
  
  You build upData (or structures) are chunks of data built up from primitive bytes.

But along came object oriented programming. Now functions and the data they work on are grouped together into objects.

An object is a grouping of functions and data. Objects are little islands of data and functions in memory.

That makes it sound like OO is a harmony of pieces that work together. In reality, it is more like a parasitic infection. The data structures continue to organize bytes of memory as they always have, completely unaware that a family of functions has packed up and moved in with them. This proximity gives the functions special access to the data and the other functions on the island.

![](robot.jpg)

# Object Lifecycle

To use an object it must first be created. Some objects are created for you before your code starts running. Most object will
be created explicitly by your code.

Then, you use the objects -- you use the "dot" operator to access data and call functions on each individual island/object.

Finally, when you are done with the objects, they are destroyed. In C++, this is usually (but not always) a manual operation. In Java and Python, objects are cleaned up automatically when nobody is using them anymore.

## Examples of creating/using

`Java`

```Java
Robot rob = new Robot("Hank",22,33);
rob.moveTo(99, 88);
rob.fireLasers(0.11F);
float f = rob.getFuelLevel();
System.out.println(f);
```

`Python`

```Python
rob = Robot("Joe",50,50)
rob.move_to(40,30)
rob.fire_lasers(0.75)
f = rob.get_fuel_level()
print(f)
```

`C++`

```C++
Robot * rob = new Robot("sue", 20, 30);
rob->fireLasers(0.5);
rob->moveTo(5, 5);
float f = rob->getFuelLevel();
cout << f << endl;

Robot r("jan", 100, 200);
r.fireLasers(1.0);
r.moveTo(0, 0);
f = r.getFuelLevel();
cout << f << endl;
```

Notice that C++ has two ways of working with objects. The first way uses the "arrow" operator "->" and works like Python and Java.

The second way uses the "dot" operator for objects that are nested inside one another or for objects that live on the stack. 
Neither Python nor Java have this ability, and we'll look at what it means later in another lesson.

# Objects have internal state

we told the robots to go to