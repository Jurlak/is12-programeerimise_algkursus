#!/usr/bin/env python
# -*- coding: utf-8 -*-
w = 10
h = 10
y = 1

while y <= h:
	x=1
	y = y + 1
	while x <= w:
		if (x+y) % 2 == 0: 
			print "##",
		else :
			print "$$",
		x = x + 1	
	print
