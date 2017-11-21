#!/usr/bin/env python3
#filename='/home/shiyanlou/calculator.py'
#f=open(filename)

def cal_tax(id,salary):
	tax_rate=0.835
	social_rate=0.165
	JiShuL=2193
	JiShuH=16446
	if salary<=JiShuL:
		social_tax=JiShuL*social_rate	
		base_salary=salary-social_tax
		base_tax=0
	elif JiShuL<salary<JiShuH:
		base_salary=salary*tax_rate
		base_tax=base_salary-3500
	else:
		social_tax=JiShuH*social_rate	
		base_salary=salary-social_tax
		base_tax=base_salary-3500

#calculate paytax;
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
	
#print acutal salary	
	acutal_salary=base_salary-pay_tax
	print (id+':'+format(acutal_salary,".2f"))

#main function
import sys
try:
	args=sys.argv[1:]
	index1=args.index('-c')
	configfile=args[index1+1]
	with open(configfile) as file:
		for x in file:
			
#	print(index1,configfile)
	index2=args.index('-d')
	userdatafile=args[index2+1]
#	print(index2,userdatafile)
	index3=args.index('-o')
	outputfile=args[index3+1]
#	print(index3,outputfile)

#raise errors
except ValueError:
	print("Parameter Error")

'''
import sys
try:
	for arg in sys.argv[1:]:
		employee=arg.split(':')
		#salary=employee[1]
		#int(salary)
#raise ValueError()
		employee_salary=int(employee[1])
		#salary=int(employee[1])
	        
		cal_tax(employee[0],employee_salary)
except ValueError:
	print("Parameter Error")
'''

