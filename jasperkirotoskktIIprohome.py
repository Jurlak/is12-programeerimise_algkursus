#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#KT II 
#1) IF - ELIF - ELSE

print "a - Eesti pealinn"
print "b - Eesti rahvaarv"
print "c - Eesti president"
print "d - Eesti pindala"


valik = raw_input('Palun valige loetelust yks t2ht : ')

a = "Eesti pealinn on Tallinn"
b = "Eesti rahvaarv on 1 286 540"	
c = "Eesti president on Toomas Hendrik Ilves"
d = "Eesti pindala on 45 227 km²"


if valik == "a":
	print a
elif valik == "b":
	print b
elif valik == "c":
	print c
elif valik == "d":
	print d
else:
	print "Vale sisend !"	
'''
#2)WHILE

n = int(raw_input(' Palun sisestage täisarv: '))

x=0 
while x<n:
	if x < n :
		print n 
	else:
		print ""
	x = x + 1
