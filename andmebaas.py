#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

cardb= { 'auto mark' : 'VW', 'auto mudel' : 'Phaeton', 'kytuse liik' : 'diisel', }

def add():
	print cardb.keys()
	cardb[raw_input('kirjutage mingi omadus: ')]=raw_input('kirjutage omadusele vastav tekst')

def rm():
	print cardb.keys() 
	del cardb[raw_input('valige ja kirjutage: ')]

def ls():
	print cardb		

def quit():
	sys.exit()

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
