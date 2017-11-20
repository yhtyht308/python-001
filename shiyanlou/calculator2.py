#!/usr/bin/env python3
#filename='/home/shiyanlou/calculator.py'
#f=open(filename)

import sys
try:
	
	for arg in sys.argv[1:]:
		employee=arg.split(':')
		salary=employee[1]
		int(salary)
#raise ValueError()

		salary=int(employee[1])
#print (salary)
		tax_rate=0.835
		base_salary=salary*tax_rate
		base_tax=base_salary-3500

		if base_tax<=0:
			pay_tax=0	
			
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
	
		acutal_salary=base_salary-pay_tax
		print (employee[0]+':'+format(acutal_salary,".2f"))
		

except ValueError:
	print("Parameter Error")



