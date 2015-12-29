number = raw_input('Enter your number: ')

i=0
while i < 10.0:
	i=i+0.000001
	print(i)
#	if (i * i) == int(number) :
#		print(i)
	if (number - i) >= i : 
		print(i)

 