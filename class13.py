"""
REMOVING elements from list


x = [1, 2, 3, 4, 5, 6, 7]
y = x.remove(4)
print(x)
OUTPUT :
aryan@Aryans-MacBook-Air Coding_seekho % /usr/local/bin/python3 /Users/aryan/Coding_seekho/class13.py
[1, 2, 3, 5, 6, 7]

but remove function se saara 4 remove ho gya so if we want to remove 4 at any specific position it cannnot do that + it only removes first indexed value like which value comes first i.e. first matched element is removed

del x[]
y = [1, 5, 2, 3, 4, 5, 8, 9]
del y[4]
print(y)

pop()

clear()


# NESTED LIST --> LIST KE ANDAR LIST ; x = [[L1],[L2],[L3]]
x[l1][2] -> for accessing list 1


y = [[1, 5, 2], [3, 4, 5], [8, 6, 9]]
sum = 0
for i in range(0, 3):
    for j in range(0, 3):
        sum = sum + y[i][j]
print(f"sum is {sum}")
OUTPUT: aryan@Aryans-MacBook-Air Coding_seekho % /usr/local/bin/python3 /Users/aryan/Coding_seekho/class13.py
sum is 43


"""
