"""l = [1, 2, 3, 4, 5, 6, 7, 2, 3, 7, 8, 9, 21, 5, 6, 7]
for i in l:
    count = 0
    for j in l:
        if i == j:
            count += 1
    if count % 2 == 0:
        print(i)


using list

l = [1, 2, 3, 4, 5, 6, 7, 2, 3, 7, 8, 9, 21, 5, 6, 7]
freq = []
for i in range(30):
    freq.append(0)
for i in l:
    freq[i] += 1
for i in range(30):
    if freq[i] != 0 and freq[i] % 2 == 0:
        print(i)
 using dictionary

l = [1, 2, 3, 4, 5, 6, 7, 2, 3, 7, 8, 9, 21, 5, 6, 7]
d={}


"""
