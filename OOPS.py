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
