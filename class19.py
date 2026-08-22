"""
d = {"a": 1, "b": 2, "c": 3}
print( del("c"))

keys= collection of dictionary key
values= collection of all values of a dictionary
items= keys,values


d = {"b": 2, "name": "coding"}
d["name"] = "coding"
print(d.popitem())  # last me jo add hoga usko remove kr dega


d = {"a": 1, "b": 2, "c": 3}
print(d.keys())
print(d.values())
print(d.items())
print(d.get("a"))# for accessing the value of a dictionary using its key

# accessing key and values using loops method - 1
d = {"a": 1, "b": 2, "c": 3, "d": 4}
for x in d.keys():
    print(x)
    print(d.get(x))

# accessing key and values using loops method - 1
d = {"a": 1, "b": 2, "c": 3, "d": 4}
for x in d.values():
    print(x)

    # accessing key and values using loops method - 1
d = {"a": 1, "b": 2, "c": 3, "d": 4}
for x, y in d.items():
    print(x)
    print(y)
# output
a
1
b
2
c
3
d
4

# NESTED DICTIONARY
student={"name":"aryan",
         "age":"21",
         "batch":"DA"
         "address":{"city":"LUCKNOW",
                    "state":"UP",
                    "pincode":"660603"
         }

         }


d = {"a": 1, "b": 2, "c": 3}
print(len(d))
key = d.keys()
d.popitem()
print(len(d))
print(len(key))
#OUTPUT:
aryan@Aryans-MacBook-Air Coding_seekho % /usr/local/bin/python3 /Users/aryan/Coding_seekho/class19.py
3
2
2
"""
