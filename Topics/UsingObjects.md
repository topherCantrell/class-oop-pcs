# Working with Objects: This course in a nutshell

Is a car an object? What does a car have?
  - motor
  - wheels
  - brakes
  - doors

But do you really care? As a user of a car, you really care about what the car can do for you:
  - setSpeed
  - blowHorn
  - start
  - stop

Objects have physical parts and objects have behavior. Both are important, but when you are
working with an object, it is all about the behavior.

As a programmer, you tell objects to do things. How do you speak to an object? "Telling" means 
calling one of the object's functions. An object has functions (we call these methods), which
are its behaviors.

Calling the "X" method on the "car" object.

car.start()
car.setSpeed(50)
car.blowHorn(2)
car.stop()
x = car.getSpeed()

What language is this? Could be most any. They look the same. Object on the left. Dot. Then
function (behavior or method). 

Objects can return information to the caller. This makes sense -- the behaviors are functions,
and we know functions can return a value.

This lets us isolate related code into objects -- keep the similar things together instead of
having global functions smeared all over the code.

turnTable.setVolume()
turnTable.start()
turnTable.stop()

All the "turn table" stuff is together and all the "car" stuff is together --- nice and encapsulate. This is one of the key points of OOP. We'll see how encapsulation works
in detail.

Same start, stop. So imagine this code:

// o is an object of some kind ... not sure where it came from
o.start()
sleep(30)
o.stop()

It works with turnTables and cars. And (potentially) any object that has a start and stop.

This is polymorphism -- another key point of OOP. Very powerful, and in this case 
dangerous. We'll see how to code object class hierarchies and relationships.