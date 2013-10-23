# -*- coding: UTF-8 -*-

def keskmine():
    esimene=(raw_input("Sisestage esimene arv: "))
    if esimene=="":
        print "Ei sisestatud esimest arvu"
        return keskmine()
    teine=int(raw_input("Sisestage teine arv: "))
    if teine=="":
        print "Ei sisestatud teist arvu"
        return keskmine()
    summa = float(int(esimene)+int(teine))
    b=float(int(summa)/2.0)
    print ("Nende arvude keskmine on "+str(b))

    print "###############################################################"



def fjada():
    arv=input("Sisestage üks number, peale mida kuvatakse fibonacci jada:")
    esimene, teine = 0, 1
    while esimene<arv:
        print esimene,
        esimene, teine = teine, esimene+teine


    print "###############################################################"   

def ruutfunktsioon():
    print "Ruutfunktsioon näeb välja nii\n ax(ruut)+bx+c=0\n anna väärtused a-le, b-le ja c-le\n ja peale seda kuvatakse teile ruutfunktsioon koos vastustega"
    print "###############################################################"
    a=raw_input("Sisestage a väärtus, sisestamisel pane arvu ette kas - või + märk!: ")
    b=raw_input("Sisestage b väärtus, sisestamisel pane arvu ette kas - või + märk!: ")
    c=raw_input("Sisestage c väärtus, sisestamisel pane arvu ette kas - või + märk!: ")
    print "###############################################################"
    print 'Te sisestasite ruutfunktsiooni mis näeb välja nii, ' +a+'x(ruut)'+b+'x'+c+'=0'
    juur=((int(b)*int(b))-4*(int(a)*int(c)))
    ac=(4*(int(a)*int(c)))
    b2=((int(b)*int(b)))
    aa=(int(a)*2)
    if int(juur)<int(ac):
        print "Sellel ruutfunktsioonil lahendid puuduvad, kuna juur ei lahene!"
    else:
        ruutjuur=int(juur)**.5
        x1=(-(float(b))-int(ruutjuur))
        x2=(-(int(b))+int(ruutjuur))
        k1=float(x1)/float(aa)
        k2=(float(x2)/float(aa))
        print k1,k2
        x1=round(float(x1)/float(aa),2)
        x2=round(float(x2)/float(aa),2)
        kontroll1=round((float(a)*float(k1)*float(k1))+(float(b)*float(k1))+float(c),0)
        v1=int(kontroll1)
        print v1
        kontroll2=round((float(a)*float(k2)*float(k2))+(float(b)*float(k2))+float(c),0)
        v2=int(kontroll2)
        print v2
        if v1==0 and v2==0:
            print "Ruutfunktsiooni lahendid on:"+str(x1)+" ja "+str(x2)
        elif v1==0 and v2!=0:
            print "Ruutfunktsiooni lahend on:"+str(x1)+" ja "+str(x2)+ " on võõrlahend"
        elif v1!=0 and v2==0:
            print "Ruutfunktsiooni lahend on:"+str(x2)+" ja "+str(x1)+ " on võõrlahend"
        else:
            print "Lahendeid ei ole"

keskmine()
fjada()
ruutfunktsioon()



