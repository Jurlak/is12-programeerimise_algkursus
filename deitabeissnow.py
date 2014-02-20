#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

cardb= [


['VW', 'Phaeton', 'diisel'],
['BMW', '750', 'bensiin'],
['Volvo', 'S80', 'diisel'],
['Audi', 'A7', 'diisel'],
['Mercedes-Benz', 'SL 500', 'diisel'],
]

x=len(cardb)


def add():
		cardb.insert(x,[raw_input("Sisestage automark: "), raw_input("Sisestage auto mudel: "), raw_input("Sisestage kütuse liik: ")]) 

def rm():
		for element in cardb:
			print element
		cardb.pop(int(raw_input("sisestage number 0-..., et mõni automark eemaldada: ")))

def ls():
		for element in cardb:
			print element		

def quit():
		sys.exit(0)

while True:
		print " "
		print "add- lisab andmebaasi masiivi"
		print "rm- eemaldab masiivist teatud rea"
		print "ls- kuvatakse andmebaas"
		print "q- lahkuge andmebaasist"
		print " "
		
		kys = raw_input("Sinu valik? ")
		if kys == "add":
				add()
		elif kys == "rm":
				rm()
		elif kys == "ls":
				ls()
		elif kys == "q":
				quit()
		else:
				print " Vale sisestus, proovige uuesti ! "
