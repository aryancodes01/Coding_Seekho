"""n = int(input("Enter the rows:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
"""

"""n = int(input("Enter the rows:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or i == n or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
 OUTPUT :
Enter the rows:5
* 
* * 
*   * 
*     * 
* * * * * 
"""
"""n = int(input("Enter the number:"))
for i in range(n):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
    OUTPUT:
        
        * 
      * * * 
    * * * * * 
  * * * * * * * 
"""
"""n = int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    for l in range(i - 1, 0, -1):
        print(l, end=" ")
    print()
    OUTPUT:
    Enter the number:5
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
"""
# CHARACTER PATTERNS
"""n = int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(65 + j - 1), end=" ")
    print()
    OUTPUT:
    Enter the number:5
A 
A B 
A B C 
A B C D 
A B C D E 
"""
