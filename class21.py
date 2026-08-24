"""
>>>>>FUNCTION is a block of code which performs specific task and it helps to reduce the code by using reusability concept and also helps the breaking of programs by modularity concepts.

Functions |---->>built in or predefined
          |---->>User defined

function syntax --->  def FunCtion():

function callling -----> FunCtion()

ARGUMENTS AND PARAMETERS
 def add(x,y):
    print(x+y)
 add(2,3)

WHERE x,y = parameters & 2,3= arguments

Agar funtion kuch nhi return krega to wo none return krega

def Add(x, y):
    return x + y, x - y


z = Add(2, 3)
print(z)

it returns tuple (5, -1)


def Add(x, y):
    return x + y, x - y, x * y


(
    z,
    *p,
) = Add(2, 3)
print(z)
print(*p)

o/p=  5
      -1 6


x = 3


def function(x):
    print(x)


print(function(2))
print(x)

o/p=  2
      None
      3



"""

l = [1, 2, 3, 4]


def sqF():
    for x in l:
        print(x * x)


sqF()
