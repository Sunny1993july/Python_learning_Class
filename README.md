This is use to a short notes regarding the Classes of the Python.

# Class
- It is a blueprint for creating objects.
- It is use to model complex data structures and behaviours in modular way.
-  ***Object*** is the instances of the class.
- Each instance of the class can have its own values
- Each instance can have different behaviors.
- ***Object's state*** is class instance has its own properties.
- ***Attributes*** is term refers to the properties / data associted with
  a specific objec of the given class (in general OOP).
  In python, attributes are the *variables* inside a class and is use
  to the store the data relate to the class.
- ***Method*** is the function within the class which is responsible for its behaviour.
- ***Member*** = *attributes* + *methods*
## Basic syntax
>
>from math import pi
>
>class Circle:
>    def __init__(self, radius):
>        self.radius = radius
>
>    def area_caculation(self):
>        return pi * (self.radius)**2 
>

  -  ***.__init__()*** method is called object's *initializer*.
  -   It defines and sets the initial values for the objects' attributes.

## Creating objects using Class
   - *** Instantiation *** is creating new object from the existing class.
   - With every new instantiation create new object.
   - The class is instantiate in the given below way.
     It is done by the calling the ***class constructor*** Circle and its accept the same
     arguments *.__init()*  class.
      > 
      >   circle = Circle(43)
      >
      >   print(circle)   
      >
      >   
      
   - This is the result of the code excution. 
      > 
      >    Mon 28 Jul - 17:05  ~/Desktop/Programming/Python/Class   master 2● 2✚ ⚑ 
      >    @kamaljeet-singh  python3 Class.py
      >    <__main__.Circle object at 0x7ac57c336900> # the memory address of the class
      >    (venv)   
      > 

## Accessing the Members
- The ***dot operator*** with ***dot notation*** is use to access the *member* of the class.
  >
  > obj.attribute_name -> it returns the attribute of the class.
  > obj.method_name() -> it use to call the class method.
  >
- It is also use to change the current values of the Class *i.e.* change the *state* of the class
  >
  >Class.attribute_name = values
  >

## Name Mangling
- The members of the class with ***__value/method***  are non public member are use for internal process.
- To prevents name from clashing with inheritance.

# Benefits
- Models and solve complex real-world problems.
- Reuse the code and avoid repetitation.
- Encapsulate related data and behaviours in a single entity.
- Abtracts way the implemented Class of the library.
- Use polymorphsim to create several slightly differnt class using one base class

# When not to use ***Class***
- ***To store***.
- If only ***one method*** is in the Class.

### Class Attribute
- This is the variable define in the Class directly. 
- This data is comman to all the methods and all the instantiated class.

### Instance attribute
- A variable defined inside an instance method using *self argument* and *dot notation*.

### Methods
- The Python Class are of three different class:
  -  ***Instance Method***: Takes *self* as the first arguments.
  -  ***Class Method***: Takes *current Class* as first arguments.
  -  ***Static Class***: Takes neither as the arguments.

### Instance Method
- This is to 


