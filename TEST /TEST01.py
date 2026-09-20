""" 1. Second Largest Unique Number
You are given a list of integers. Find the second largest unique number in the list.
If there is no second largest unique number, print "Not Possible".
Example 1:
InD, [20, 4, 20, 15, 10, 8]
Output:
15
Example 2:
Input:
[5, 5, 5]
Output: Not Possible
"""
  
a = [20, 4, 20, 15, 10, 81]
b = []

for i in a:
    if i not in b:
        b.append(i)

b.sort(reverse=True)


  
  
  
"""4. Student Marks Analysis
You are given the marks of students in a list.
marks = [78, 45, 90, 32, 67, 89,50, 92]
Write a program to:
1. Find the highest marks.
2. Find the lowest marks.
3. Calculate the average marks.
4. Count the number of students who passed.
5. Count the number of students who failed.
A student is considered passed if marks >= 40.
Expected Output:
Highest: 92
Lowest: 32
Average: 67.875
Passed: 7
Failed: 1"""
marks = [78, 45, 90, 32, 67, 89, 50, 92]
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
passed = 0
failed = 0
for m in marks:
    if m >= 40:
        passed += 1
    else:
        failed += 1

print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {average}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")

"""3. Remove Duplicate Elements Without Using set)
You are given a list containing duplicate values.
Create a new list containing each value only once, while maintainingthe original SEEKHO
order.
You are not allowed to use set () .
Example:
Input:
[10, 20, 10, 30, 20, 40, 30]
Output:
[10, 20, 30, 40]"""
a = [10, 20, 10, 30, 20, 40, 30]
b = []

for i in a:
    if i not in  b:
        b.append(i)

print(b)


"""7. Find the First Non-Repeating Character
Given a string, find the first character that occurs only once.
If every character is repeated, print "No unique character".
Example 1:
Input:
"aabbedde"

Output :
Example 2:
Input: "aabbcc"
Output:
"No unique character"""

s = "aabbedde"

for i in s:
    if s.count(i) == 1:
        print(i)
        break
else:
    print("No unique character")
    
