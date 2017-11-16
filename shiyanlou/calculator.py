#!/usr/bin/env python3
#filename='/home/shiyanlou/calculator.py'
#f=open(filename)

try:
	import sys
	int(sys.argv[1])
#	raise ValueError()

	salary=int(sys.argv[1])
	#print (salary)

	base_tax=salary-3500

	if base_tax<=0:
		pay_tax=0	
		print (pay_tax)
	elif 0<base_tax<=1500:
		pay_tax=base_tax*0.03-0
	elif 1500<base_tax<=4500:
		pay_tax=base_tax*0.10-105
	elif 4500<base_tax<=9000:
		pay_tax=base_tax*0.20-555
	elif 9000<base_tax<=35000:
		pay_tax=base_tax*0.25-1005
	elif 35000<base_tax<=55000:
		pay_tax=base_tax*0.30-2755
	elif 55000<base_tax<=80000:
		pay_tax=base_tax*0.35-5505
	else:
		pay_tax=base_tax*0.45-13505

	print (format(pay_tax,".2f"))

except ValueError:
	print("Parameter Error")



