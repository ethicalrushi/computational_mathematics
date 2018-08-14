
#Returns the function value for given x

def funcn(a,b,c,x):

	#You can change the functon definition here
	val = a*x*x+b*x+c 
	return val





#Bisect function 
def bisect(a,b,c,error,x1,x2):
	#bisecting the range
	x3 = (x1+ x2)/2

	#Checking the error to terminate the iterative process
	if(abs(funcn(a,b,c,x3)) <= error):
		return x3
		

	# If error is not tolerable then continue the iterations
	else:
		#Checking the interval for which function vaues are opposite
		if(funcn(a,b,c,x3)*funcn(a,b,c,x1)<0):
			x2 = x3
		else:
			x1 = x3
		#another iteration
		return bisect(a,b,c,error,x1,x2)




def main():
	#Taking multiple string input separatred by a space
	a,b,c = input('Enter a,b,c:').split()
	#Cnverting to integers
	a = int(a)
	b = int(b)
	c = int(c)
	
	prec = int(input('Enter digits of precision:'))
	x1, x2 = input('Enter x1 and x2 the range for first approximation:').split()
	x1 = int(x1)
	x2 = int(x2)

	#Calculating error tolerance for given precision
	error = (1/2)*10**(-prec)
	
	if(abs(funcn(a,b,c,x1))<=error):
		print(x1)
	else :
		if(abs(funcn(a,b,c,x2))<=error):
			print(x2)
		else:
			if(funcn(a,b,c,x1)*funcn(a,b,c,x2)<=0):
				result = bisect(a,b,c,error,x1,x2)
				print(result)
			else:
				print("Invalid range")
	return 0







if __name__ == '__main__':
	main()