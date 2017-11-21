#!/usr/bin/python3

import sys 
args=sys.argv[1:]
index1=args.index('-c')
configfile=args[index1+1]
print(index1,configfile)
self_config={}
with open(configfile,'r') as file:
	for c in file:
		c=c.strip('\n')
		c=c.split('=')
		key=c[0].strip()
		value=c[1].strip()
		self_config[key]=value
print(self_config)
