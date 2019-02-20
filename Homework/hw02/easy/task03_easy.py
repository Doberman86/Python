numbers = [1,3,3,4,5,6,3,7,5,34,23,5,6,78,99]

nl = []
for l in numbers:
    if l % 2 == 0:
        nl.append(l/4)
    else:
        nl.append(2*l)

for l in nl:
    print(l)