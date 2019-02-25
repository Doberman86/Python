import math

listA = [2, -5, 8, 9, -25, 25, 4]

listB = []
for l in listA:
    root = math.floor(math.sqrt(abs(l)))
    rooted = root**2 - l
    nonnegative = (l >= 0)
    if not(rooted) and nonnegative:
        listB.append(root)

for l in listB:
    print(l)