
fruits = ['яблоко', 'банан', 'киви', 'арбуз']
i = 0

while i < len(fruits):
	print(i+1, '{0:>10}'.format(fruits[i]))
	i +=1
else:
	print("Все верно!!!")
	