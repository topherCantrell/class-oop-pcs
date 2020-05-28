# Object Oriented Programming: A Multi-Language Examination

Links:
  - https://en.wikipedia.org/wiki/Imperative_programming
  - https://en.wikipedia.org/wiki/Object-oriented_programming
  - https://developers.slashdot.org/story/19/07/22/0426201/is-object-oriented-programming-a-trillion-dollar-disaster
  
Books:
  - [Design Patterns](https://www.amazon.com/dp/0201633612?tag=bizzi0d-20)
  - https://www.amazon.com/Fundamental-Concepts-Object-Oriented-Programming-ebook/dp/B00FO496ZW/ref=sr_1_13
  - [The OO Thought Process](https://www.amazon.com/dp/B004Z6EWBI?tag=bizzi0d-20)
  
1. The "dot" operator. Islands of data and functions

| Lecture                           | Status                 |
| ----                              | ----                   |
| ### M1_Encapsulation ######       | ###################### |
| 01_Islands_of_data                |                        |
| EX_1a_Modeling                    |                        |
| 02_Evolution_of_OO                | **40 mins**            |
| EX_1b_UsingObjects                |                        |
|                                   |                        |
| 03_Constructors_and_destructors   |                        |
| EX_2a_TBD                         |                        |
| 04_Statics_and_operators          |                        |
| EX_2b_TBD                         |                        |
|                                   |                        |
| 05_TicTacToe_example              | **30 mins**            |
| EX_3a_FleshOutTicTacToe           |                        |
| 06_Memory_and_pointers_and_CPP    |                        |
| EX_3b_FleshOutTicTacToe           |                        |
|                                   |                        |
| ### M2_Inheritance ######         | ###################### | 
| 07_Inheritance_polymorphism       |                        |
| EX_4a_TBD                         |                        |
| 08_Multiple_inheritance           |                        |
| EX_4b_TBD                         |                        |
|                                   |                        |
| 09_AnimalTalker_TTTPlayer_example |                        |
| EX_5a_TBD                         |                        |
| 10_Collections                    |                        |
| EX_5b_TBD                         |                        |
| 
| ### M3_Design_patterns ######     | ###################### |
| 11_Design_patterns                |                        |
| EX_6a_TBD                         |                        |
| 12_Streams                        |                        |
| EX_6b_TBD                         |                        |
|                                   |                        |
| ### M4_UML_and_OOAD ######        | ###################### |
| 13_UML_and_terminology            |                        |
| EX_7a_TBD                         |                        |
| 14_OOAD                           |                        |
| EX_7b_TBD                         |                        |



# Module 1: Encapsulation

## M1_1_Evolution_of_OO
  - 3,4: Assembly language, how IFs work, labels, subroutines, assembler is forerunner to compiler
  - 5: RAM, ROM, IO, stack, heap, function information on the stack
  - 6: Structured programming, subroutines, no-goto, disassembly of a loop, disassembly of an expression
  - 7,8: Virtual machines, python is compiled
  - 9: Memory structure
  - 10: Functions coupled to structure
  - 11, 12: Encapsulation, basic objects, access keywords
  - 13: "this" in python
  - 14: Nesting structures (composition)
  - 15,16: Basic inheritance
  - 17: Pointers to functions
  - 18, 19: Virtual function table, polymorphismm
    
## M1_2_Classes_and_objects
  - What time is it
  - Program to the interface -- not the implementation (more later)    
    
  - Interface/API
  - Software Reuse
  - NamingConvention/Verbs/nouns/best-practice
    
## M1_3_Statics_and_members
   - Getters and Setters
   - Constructors/Destructors
   - Construction -- special time in an object's life. Initialize vs set
     
## M1_4_TicTacToe_example
  - 3: Finding the objects
  - 4: Design in comments
  - 5,6: Argument and return types -- enums, ranges
  - 7: Functional implementation
  - 8,9: Problems with functional design
  - 10: Finding objects (again), coupling
  - 11: UML example
  - 12: The "using" code
  - 13: The "Board" class
  - 14: Unit tests on "Board"
  - 15: Player
  - 16: Challenge: how to select type of players (hint of polymorphism)

## M1_5_Memory_and_pointers
  - heap and stack
  - following pointers
  - garbage collection

## M2_3_Program_to_interface 
  - Interface vs Implementation
  - RandomPoint example

## M2_4_Composition_and_diamond_of_death

## M2_5_Java_collections

## M2_6_Cpp_Collections

## M2_7_Streams_Example

## ?? TicTacToe revisited

# Module 3: Design Patterns

## M3_2_Singleton

## M3_3_Decprator_Proxies

# Module 4: UML and OOAD

## M4_1_Terminology
  - super, base, derived, sub-class, is-a, has-a

## Maybe include  
  - SOLID and GRASP guidelines
  - UML modeling
    
# Work these in
  - M1_1_OO vs Functional`
  - M2_6_GUI_Callback_functional_alternatives
  - Anonymous
  - Inner
  - Private inheritance
  - Software reuse (project structure to share code)

  
  - OO vs functional
  - composition by pointers in java/python
  - M4_3_SOLID_GRASP_DRY
  - M4_4_OO_vs_Functional
  - M4_5_GUI_Callback