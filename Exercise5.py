import random

#  ------ normal exercise ------
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)

#  ------ 1. extra exercise ------

d = random.sample(range(1, 50), k=random.randint(5, 15))
e = random.sample(range(1, 50), k=random.randint(5, 15))

f = []

for i in d:
    if i in e and i not in f:
        f.append(i)
print(f)

# ------ 2. extra exercise ------

print(list(set(d) & set(e)))
