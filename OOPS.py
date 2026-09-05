"""
Phle ye hota tha ki maan lo student  hai to uska roll no . hoga class hoga aise bhot saare students honge to agr sabko staore krenge ek hi variable me to value update hoti jayegi and agr hm maan lo dictionary bhi bna li to variable to same rkh lenege but 1000 students ke liye to 1000 dictionary bnani pdegi jo ki bhot dikkat kregi ----- so isi ke liye oops concept bnaya gya!!!

FOR class and object creation -->
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self)
        print("object is created ")


obj1 = Student("CODING SEEKHO", "9.5")
obj2 = Student("CODING", "10")
print(obj1.name)
print(obj2.age)


4 PILLLARS:
1. ENCAPSULATION
2. INHERITANCE
3. ABSTRACTION
4. POLYMORPHISM


A method is simply a function that belongs to a class.

class Student:
    def study(self):
        print("Student is studying")

s1 = Student()
s1.study()

Output:

Student is studying

Here:

Student → class
study() → method
s1 → object
self → refers to the current object
Types of Methods in Python

There are 3 main types of methods:

Instance Method
Class Method
Static Method
1. Instance Method

An instance method works with the object/instance of a class.

It normally takes self as its first parameter.

class Student:
    def show(self):
        print("I am a student")

s1 = Student()
s1.show()
Using instance variables
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

s1 = Student("Aryan", 21)
s1.display()

Here display() is an instance method because it uses self.

Remember:

Instance Method → self → Object

2. Class Method

A class method works with the class itself, rather than a particular object.

It uses cls as its first parameter and is created using the @classmethod decorator.

class Student:
    college = "Lucknow University"

    @classmethod
    def show_college(cls):
        print(cls.college)

Student.show_college()

Output:

Lucknow University

Here:

cls.college

accesses the class variable.

Can also be called using an object:
s1 = Student()
s1.show_college()
Remember:

Class Method → cls → Class

3. Static Method

A static method does not depend on the object or class.

It is created using @staticmethod.

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))

Output:

30



class student:
    college = "coding seekho"

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def showdata(self):
        print(self.name)

    @classmethod
    def showcollegename(cls):
        print(cls.college)


obj = student("aryan", 10)

obj.showdata()

"""


class Student:
    class_var = "adbc"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self)
        print("object is created ")


obj1 = Student("CODING SEEKHO", "9.5")
obj2 = Student("CODING", "10")
print(obj1.name)
print(obj2.age)
print(obj1.class_var)
