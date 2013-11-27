#!/usr/bin/env python
# -*- coding: utf8 -*-

#1)Ül


tekst = raw_input("Palun sisestage üks tekst!: ")

if tekst == str(tekst.lower()) and any(c.isdigit() for c in tekst):
	print "Väiketähed ja numbrid!"

elif tekst == str(tekst.lower()):
	print "Väiketähed ja numbriteta!"

elif tekst == str(tekst.upper()) and any(c.isdigit() for c in tekst):
	print "Suurtähed ja numbrid!" 

elif tekst == str(tekst.upper()):
	print "Suurtähed ja numbriteta!"

elif any(c.isdigit() for c in tekst):
	print "Suur-väiketähed ja numbrid!"

else:
	print "Suur-väiketähed ja numbriteta!"




#2)Ül


arv1 = int(raw_input("Sisestage esimene arv!: "))
arv2 = int(raw_input("Sisestage teine arv!: "))
ax = 3
def arvud(arv1, arv2, ax):
	if arv1 > arv2:	
		arv1,arv2 = arv2,arv1	
		arv1 = arv1 + (ax - (arv1 % ax))
		return [i for i in range(arv1, arv2, ax)]

tulemus = [i for i in range((arv1 + (ax - (arv1 % ax))),arv2, ax)]
print "Arvude vahel on " + str(len(tulemus)) + " arvu, mis jaguvad 3-ga"

