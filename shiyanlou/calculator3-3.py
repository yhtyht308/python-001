#!/usr/bin/env python3
#filename='/home/shiyanlou/calculator.py'
#f=open(filename)

def cal_tax(t_rate,s_rate,JSL,JSG,Id,salary):
#	tax_rate=0.835
#	social_rate=0.165
#	JiShuL=2193
#	JiShuH=16446
	tax_rate=t_rate
	social_rate=s_rate
	JiShuL=JSL
	JiShuH=JSG
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
	social_tax1=social_tax
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
	print (Id+':'+format(acutal_salary,".2f"))

	tax_after=float(acutal_salary)
	output_function(Id,salary,social_tax1,pay_tax,tax_after)

def config_function(Id,salary):
	
	index1=args.index('-c')
	configfile=args[index1+1]
	self_config={}
	with open(configfile) as file:
		for c in file:
			c=c.strip('\n')
			c=c.split('=')
			key=c[0].strip()
			value=c[1].strip()
			self_config[key]=value
#		print(self_config)
	JSL=float(self_config['JiShuL'])
	JSH=float(self_config['JiShuH'])
	s_rate=float(self_config['YangLao'])+float(self_config['YiLiao'])+float(self_config['ShiYe'])+float(self_config['GongShang'])+float(self_config['ShengYu'])+float(self_config['GongJiJin'])
	t_rate=1-s_rate
	#cal_tax(t_rate,s_rate,JSL,JSH,id='200',salary=25000)
	cal_tax(t_rate,s_rate,JSL,JSH,Id,salary)		
	#	print(index1,configfile)

def output_function(Id,Sal,Social_tax,Pay_tax,Tax_after):	
	index3=args.index('-o')
	outputfile=args[index3+1]
	with open(outputfile,'a') as file:
		file.writelines(Id+','+'%i,%.2f,%.2f,%.2f'%(Sal,Social_tax,Pay_tax,Tax_after))
		file.write('\n\n')
#	print(index3,outputfile)

#main function
import sys
args=sys.argv[1:]
#try:

index2=args.index('-d')
userdatafile=args[index2+1]
self_userdata={}
with open(userdatafile) as file:
	for u in file:
		u=u.strip('\n')
		u=u.split(',')
		key=u[0].strip()
		value=u[1].strip()
		self_userdata[key]=value
#print(self_userdata)
for key1,value1 in self_userdata.items():
	print(key1,value1)
	id1=int(key1)
	sal=int(value1)
	config_function(key1,sal)
	
#	print(index2,userdatafile)


'''
#raise errors
except ValueError:
	print("Parameter Error")
'''
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

