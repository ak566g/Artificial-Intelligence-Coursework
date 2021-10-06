n = int(input('the number of machines: '))
x = int(input('maximum speed of the motor: '))
k = 0
if (2*n-1) <= x:
	k = x
	for i in range(n-1):
		k *= x//(2*(1+i))
print(f'configuration modulus: {k}')