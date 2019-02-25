listA = ['Esc', 'Delete', 'Enter','Delete','G','U']
listB = ['CapsLock', 'Delete', 'NumLock','Tab','G','B']

for b in listB:
    count = listA.count(b)
    for index in range(0,count):
        listA.remove(b)

for a in listA:
    print(a)