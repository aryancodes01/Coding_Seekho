"""
OPERATORS IN STRING -->

# CONCATENATAION - ADDING TWO DIFFERENT STRINGS
  x = st1+" "+ st2

# REPETITION (*)
for exmaple ("hello"*3)

for i in range(1, 5):
    print("* " * i)
print()
 OUTPPUT:
aryan@Aryans-MacBook-Air Coding_seekho % /usr/local/bin/python3 /Users/aryan/Coding_seekho/class11.py
*
* *
* * *
* * * *

# IN OPERATOR - in and not in
"str1" in "str2"|----> true
                |----> false

# == operators
 "str1" == "str2" |----> true
                  |----> false

# METHODS
 Those function which are already defined in our python string .

* .lower() -> converts into lower case
* .upper() -> converts into upper case

s = "COding SeeKHo"
print(s.lower())
 OUTPUT:
aryan@Aryans-MacBook-Air Coding_seekho % /usr/local/bin/python3 /Users/aryan/Coding_seekho/class11.py
coding seekho

* title() -> first letter to uppercase
* strip() -> used to remove unwanted space from start and end of the string
* .find() -> to find any string , agr present hai to index dega agr nhi hai to -1 dega ooutput.


s = "COding SeeKHo"
print(s.find("girl"))
OUTPUT :
aryan@Aryans-MacBook-Air Coding_seekho % /usr/local/bin/python3 /Users/aryan/Coding_seekho/class11.py
-1

s = "COding SeeKHo"
print(s.find("See"))
OUTPUT:
aryan@Aryans-MacBook-Air Coding_seekho % /usr/local/bin/python3 /Users/aryan/Coding_seekho/class11.py
7
s = "COding SeeKHo"
if s.find("M"):
    print("found")
else:
    print(" not found ")
     OUTPUT:
    aryan@Aryans-MacBook-Air Coding_seekho % /usr/local/bin/python3 /Users/aryan/Coding_seekho/class11.py
found
 === aise kyu ho rha kyuki jb ye run hoga tb -1 return krega jo ki non zero value hai to if condition usko true ki tarah treat krega so ye found return krega
THIS IS THE  DRAWBACK OF FIND.

* split() -> SEPARATE KR DETA HAI  jiske behalf pe krna chaho and return krta hai lists

s = "COding SeeKHo in my class"
print(s.split(" "))
OUTPUT:
aryan@Aryans-MacBook-Air Coding_seekho % /usr/local/bin/python3 /Users/aryan/Coding_seekho/class11.py
['COding', 'SeeKHo', 'in', 'my', 'class']

* join -> used to join the string
* replace -> used to replace a string
* count -> used to count the number of times that string is present
* startswith() -> gives true or false if the condition is true or false according to the statement.
* endswith() -> gives same true or false .

s = "COding SeeKHo in my class"
print(s.startswith("C"))
 OUTPUT:
 aryan@Aryans-MacBook-Air Coding_seekho % /usr/local/bin/python3 /Users/aryan/Coding_seekho/class11.py
True

"""
