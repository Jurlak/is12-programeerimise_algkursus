from random import randint


nimekiri = ["Arti","Mariin","Janis","Art","Kerto","Timo","Jasper","Mario","Kairo","Ardo","Janar","Katerin","Rait","Aulis",]

i=1
while i<=100:
	print (nimekiri)
	arv = len(nimekiri)-1
	a = randint(0,arv)
	b = nimekiri[a]
	print(b)
	del nimekiri[a]
	print (sorted(nimekiri))
	nimekiri = ((sorted(nimekiri) + [b]))
	i=i+1
print("100 T2itus")






