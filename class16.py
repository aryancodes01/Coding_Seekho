"""
SET = collection of objects
mutable = changeable (add or remove )
no duplicate values allowed
always unique value
### creating a set

x=set()
y = {1, 2, 3, 4}
print(type(x))
print(type(y))

x = {1, 2, 3, 4}
x.add(5)
print(x)
OUTPUT: {1, 2, 3, 4, 5}


x = {1, 2, 3, 4}
x.update([6])
print(x)
OUTPUT:{1, 2, 3, 4, 6}

SET CONSTRUCTOR SEQUENCE KO SET ME BADAL SAKTA HAI

x = set("coding")
print(x)
print(type(x))
OUTPUT:
{'g', 'o', 'd', 'i', 'c', 'n'}
<class 'set'>


x = {1, 2, 3, 4}
x.discard(4)
print(x)              ---------------------------->>>>discard elment ko remove krdega agar hoga to nhi hoga to aage badh jayega error ni -------                                                dega but remove error dega
OUTPUT:{1, 2, 3}

x = {1, 2, 3, 4}
x.remove(4)
print(x)
OUTPUT:{1, 2, 3}

x = {1, 2, 3, 4}
y = {2, 9, 10}
print(x.union(y))
print(x.difference(y))
print(x.symmetric_difference(y))
print(x.issubset(y))
print(x.issuperset(y))
OUTPUT:
{1, 2, 3, 4, 9, 10}
{1, 3, 4}
{1, 3, 4, 9, 10}
False
False

x = {1, 2, 3, 4}
y = {2, 9, 10}
print(x.union(y))
print(x.difference(y))
print(x.symmetric_difference(y))
print(x.issubset(y))
print(x.issuperset(y))
print(x | y)
print(x & y)
print(x - y)

"""

s = "coding seekho is the best"
count = 0

for d in "abcdefghijklmnopqrstuvwxyz":
    for x in s:
        if d == x:
            count += 1
            break

print(count)
