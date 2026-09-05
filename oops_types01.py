"""

4 PILLLARS:
1. ENCAPSULATION
2. INHERITANCE
3. ABSTRACTION
4. POLYMORPHISM

1. ENCAPSULATION :Encapsulation means wrapping data (attributes) and methods together inside a class and controlling how that data can be accessed or modified.

class student:
    college = "coding seekho"

    def __init__(self, n, a):
        self.name = n
        self.age = a
        self._bankname = "SBI"
        self.__pin = "1101"

    def showdata(self):
        print(obj.name)# public
        print(obj._bankname) # protected
        print(obj.__pin) # private


obj = student("ARYAN", 10)
"""

"""print(obj.name) # public
print(obj._bankname)# protected 
print(obj.__pin)# private  : it will give error kyuki hm bhr se access nhi kr skte data ko kyuki ye private hai 
"""
"""obj.showdata()"""
"""

2. INHERITANCE : Inheritance is an OOP concept in which a child class acquires the properties (attributes) and methods of a parent class.
Inheritance = Reusing the features of an existing class in a new class.


Types of Inheritance in Python

Python has 5 commonly discussed types of inheritance:

1. Single Inheritance
One parent class → one child class
Simplest form of inheritance.
Example relationship: Animal → Dog
Single:        A → B

2. Multiple Inheritance
Multiple parent classes → one child class
A child class inherits features from more than one parent.
Example: Father + Mother → Child
Multiple:      A ─┐
                 ├→ C
                B ─┘

3. Multilevel Inheritance
Grandparent → Parent → Child
Inheritance occurs across multiple levels.
Example: Animal → Mammal → Dog
Multilevel:    A → B → C

4. Hierarchical Inheritance
One parent class → multiple child classes
Multiple classes inherit from the same parent.
Example: Animal → Dog, Cat, Cow

Hierarchical:    A
                / \
               B   C

5. Hybrid Inheritance
Combination of two or more types of inheritance
Usually combines structures such as multiple and hierarchical inheritance.
Hybrid:        Combination of multiple types               
"""


class student:
    college = "coding seekho"

    def __init__(self, n, a):
        self.name = n
        self.age = a
        self._bankname = "SBI"
        self.__pin = "1101"

    def showdata(self):
        print(obj.name)  # public
        print(obj._bankname)  # protected
        print(obj.__pin)  # private


obj = student("ARYAN", 10)
"""
print(obj.name) # public
print(obj._bankname)# protected 
print(obj.__pin)# private  : it will give error kyuki hm bhr se access nhi kr skte data ko kyuki ye private hai 
"""
obj.showdata()
