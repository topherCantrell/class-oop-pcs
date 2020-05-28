# Using Objects

The memory in your computer is a vast collection of functions and data. Functions are made from lines of code. Data (or structures) are chunks of data built up from primitive bytes.

For a long time in our programming history, functions and data were kept separated from one another. But along came object oriented programming. Now functions and the data they work on are grouped together into objects.

An object is a grouping of functions and data. Objects are little islands of data and functions in memory.

That makes it sound like OO is a harmony of pieces that work together. In reality, it is more like a parasitic infection. The data structures continue to organize bytes of memory as they always have, completely unaware that a family of functions has packed up and moved in with them. This proximity gives the functions special access to the data and the other functions on the island.

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