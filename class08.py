"""
------------------------------
           Pattern
------------------------------



n = int(input("Enter number of rows:"))
m = int(input("Enter number of columns:"))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print("*", end=" ")
    print()
"""

"""n = int(input("Enter the rows:"))
m = int(input("Enter the columns:"))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 2 or i == n - 1 or j == 1 or j == m:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""
"""n = int(input("Enter the rows:"))
m = int(input("Enter the columns:"))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 or i == 2 or i == n - 1 or i == n or j == 1 or j == m:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
    OUTPUT:
Enter the rows:5
Enter the columns:5
# # # # # 
# # # # # 
#       # 
# # # # # 
# # # # # 
"""
"""n = int(input("Enter the rows:"))
m = int(input("Enter the columns:"))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i % 2 == 0 or j == 1 or j == m:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()

     OUTPUT :
    Enter the rows:8
Enter the columns:6
#         # 
# # # # # # 
#         # 
# # # # # # 
#         # 
# # # # # # 
#         # 
# # # # # # 
"""
"""n = int(input("Enter the rows:"))
# m = int(input("Enter the columns:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("#", end=" ")
    print()
    OUTPUT:
    Enter the rows:6
# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 
"""
"""n = int(input("Enter the rows:"))
for i in range(1, n):
    for j in range(n - 1, 1):
        print("#", end=" ")
    print()
"""
n = int(input("Enter the rows:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
