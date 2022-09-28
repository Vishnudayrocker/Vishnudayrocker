num=int(input("enter the integer"))
d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

s = "" 
while(num):
	for r in d:
		if r <= num:
			s = s+(d[r])*(num/r)  
			num = num % r 
			break

print(s)