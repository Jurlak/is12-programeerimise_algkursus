#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys



print "add- lisab andmebaasi masiivi"
print "rm- eemaldab masiivist teatud rea"
print "ls- kuvatakse andmebaas"
print "q- lahkuge andmebaasist"
print " "
kys= raw_input("valige endale sobiv varjant: ")


cardb= [


['VW', 'Phaeton', 'diisel'],
['BMW', '750', 'bensiin'],
['Volvo', 'S80', 'diisel'],
['Audi', 'A7', 'diisel'],
['Mercedes-Benz', 'SL 500', 'diisel'],
]

x=len(cardb)


def add():
	if kys=='add':
		cardb.insert(x,[raw_input("Sisestage automark: "), raw_input("Sisestage auto mudel: "), raw_input("Sisestage kütuse liik: ")]) 

add()

def rm():
	if kys=='rm':
		print cardb
		cardb.pop(int(raw_input("sisestage number 0-..., et mõni automark eemaldada: ")))
rm()

def ls():
	if kys=='ls':
		print cardb
ls()		

def quit():
	if kys=='q':
		sys.exit(0)
quit()
