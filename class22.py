"""
QUESTION =
x = 1


def hello():
    x = 2
    print(x)

    def hello2():

        print(x)

    hello2()


print(x)
hello()

O/P=
x = 1
    2
    2

Use global keyword to decllare local variable to global

Predefined functions
Function	Purpose	Example
print()	Displays output	print("Hello")
input()	Takes user input	name = input("Enter name: ")
len()	Returns the length of an object	len("Python") → 6
type()	Returns the data type	type(10) → <class 'int'>
int()	Converts to integer	int("25") → 25
float()	Converts to float	float("3.14") → 3.14
str()	Converts to string	str(100) → "100" etc .

FUNCTIONS WITH ARGUMENTS ...

1. POSITIONAL ARGUMENT
2. Keyword Arguments
3. Variable-Length Arguments
4. Default Arguments





1. POSITIONAL ARGUMENT
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Aryan", 20)

Output:

Name: Aryan
Age: 20

2.Keyword Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Aryan")

Output:
Name: Aryan
Age: 20

3.Variable-Length Arguments
Type	                                             Symbol	             Stores data as
Variable positional arguments                      	*args	                Tuple
Variable keyword arguments	                       **kwargs	             Dictionary









4.Default Arguments

def student(name, age=20):
    print("Name:", name)
    print("Age:", age)

student("Aryan")

Output:

Name: Aryan
Age: 20


l = [1, 2, 3, 4, 56, 6, 7]


def fun(l):
    print(sum(l))
    print(max(l))
    print(min(l))
    print(sum(l) / len(l))
fun()

O/P=
79
56
1
11.285714285714286

"""
